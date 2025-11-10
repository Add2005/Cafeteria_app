from Entities.venta import Venta
from db.Conexion import Conexion

class VentaModel:
    
    def __init__(self):
        self.db = Conexion() 
        self.cursor = self.db.cursor()

    def GuardarVenta(self,cursor, venta: Venta):
        sql = '''INSERT INTO Venta (TotalVenta, FechaHora, IdCliente, IdEmpleado) 
                OUTPUT INSERTED.IdVenta 
                VALUES (?,?,?,?)'''
        cursor.execute(sql,(venta.TotalVenta, 
                                 venta.FechaHora, 
                                 venta.IdCliente, 
                                 venta.IdEmpleado))
        IdVenta = cursor.fetchone()[0]
        return IdVenta
    
    def ModificarVenta(self, venta: Venta, IdProducto):
        sql = 'UPDATE Venta SET TotalVenta = ?, FechaHora = ?, IdCliente = ?, IdEmpleado = ? WHERE IdVenta = ? '
        self.cursor.execute(sql, (venta.TotalVenta, 
                                  venta.FechaHora, 
                                  venta.IdCliente, 
                                  venta.IdEmpleado, 
                                  IdProducto))
        self.cursor.commit()
        
    #def ElimiarVenta(self, )
    
    def HistorialVentas(self):
        sql = 'SELECT * FROM Historial_Ventas'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def Historial_Fecha_ASC(self):
        sql = 'SELECT * FROM Historial_Ventas ORDER BY Fecha_Venta ASC'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def Historial_Fecha_DESC(self):
        sql = 'SELECT * FROM Historial_Ventas ORDER BY Fecha_Venta DESC'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def Historial_Total_ASC(self):
        sql = 'SELECT * FROM Historial_Ventas ORDER BY Total_Venta ASC'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def Historial_Total_DESC(self):
        sql = 'SELECT * FROM Historial_Ventas ORDER BY Total_Venta DESC'
        self.cursor.execute(sql)
        return self.cursor.fetchall()