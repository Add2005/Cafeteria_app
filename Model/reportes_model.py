from db.Conexion import Conexion

class reportesModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()     
        
    def obtener_reportes_mensuales(self):
        sql = 'select * from reportes_mensuales'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def obtener_productos_mas_vendidos(self):
        sql = 'select * from productos_mas_vendidos'
        self.cursor.execute(sql)
        return self.cursor.fetchall()