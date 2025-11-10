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
    
    def AgregarVentaCompleta(self, venta: Venta, lista_Det: list[tuple]):
        try:
            self.cursor.execute("BEGIN TRANSACTION;")
            idVenta = self.venta.GuardarVenta(venta)
            
            detVenta = [(idVenta, det[0], det[1]) for det in lista_Det]
            print(detVenta)
            
            self.detventa.AgregarDetVenta(detVenta)
            
            self.cursor.commit()
            print(f"Venta {idVenta} agregada correctamente con sus detalles.")
        except Exception as ex:
            self.cursor.rollback()
            messagebox.showerror("Error", f"Error en la transacción\nCod_Error: {ex}")
        finally:
            self.cursor.close()
            self.db.close()

