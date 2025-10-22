from Entities.venta import Venta
from db.Conexion import Conexion

class VentaModel:
    
    def __init__(self):
        self.db = Conexion() 
        self.cursor = self.db.cursor()
        
    def GuardarVenta(self, ):
        sql = ''
        self.cursor.executemany(sql,())