from Entities.detalle_venta import detalle_venta
from db.Conexion import Conexion

class DetalleVentaModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()

    def AgregarDetVenta(self, lista_detventa: list[tuple]): 
        sql = 'INSERT INTO DetalleVenta (IdVenta, IdProducto, Cantidad) VALUES (?,?,?)'
        self.cursor.executemany(sql, lista_detventa)
    
    def EliminarDetVenta(self):
        pass
    
    def ModificarDetVenta(self):
        pass
    
    def BuscarDetVenta(self):
        pass