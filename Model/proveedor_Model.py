from db.Conexion import Conexion
from Entities.proveedor import Proveedor

class ProveedorModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor
        
    def CargarProveedor(self):
        sql = 'SELECT * FROM Proveedor'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    