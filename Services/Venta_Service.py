from Entities.venta import Venta
from Entities.detalle_venta import detalle_venta
from Model.venta_Model import VentaModel
from Model.detVenta_Model import DetalleVentaModel
from db.Conexion import Conexion
from tkinter import messagebox

class VentaService:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()       
        self.venta = VentaModel()
        self.detventa = DetalleVentaModel()
        
    def AgregarVentaCompleta(self, venta: Venta, lista_Det: list[detalle_venta]):
        try: 
            idVenta = self.venta.GuardarVenta(self.cursor, venta)
            detVenta = []
            
            for detalle in lista_Det:
                detalle.IdVenta = idVenta
                detVenta.append(detalle.transformar_a_tupla())
                
            self.detventa.AgregarDetVenta(self.cursor, detVenta)
            self.cursor.commit() 
            
        except Exception as ex:
            self.cursor.rollback()
            messagebox.showerror("Error", f"Error en la transaccion consulte a su proveedor \n Cod_Error: {ex}")