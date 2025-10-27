from Entities.venta import Venta
from db.Conexion import Conexion

class VentaModel:
    
    def __init__(self):
        self.db = Conexion() 
        self.cursor = self.db.cursor()
    
        
    def GuardarVenta(self, venta: Venta):
        sql = 'INSERT INTO Venta (TotalVenta, FechaHora, Id_Cliente, IdEmpleado) VALUES (?,?,?,?)'
        sql2 = 'SELECT SCOPE_IDENTITY AS IdVenta'
        self.cursor.execute(sql,(venta.TotalVenta, 
                                 venta.FechaHora, 
                                 venta.Id_Cliente, 
                                 venta.Id_Empleado))
        self.cursor.execute(sql2)        
        IdVenta = self.cursor.fetchone()  
        return IdVenta
    
    def ModificarVenta(self, venta: Venta, IdProducto):
        sql = 'UPDATE Venta SET TotalVenta = ?, FechaHora = ?, Id_Cliente = ?, IdEmpleado = ? WHERE IdVenta = ? '
        self.cursor.execute(sql, (venta.TotalVenta, 
                                  venta.FechaHora, 
                                  venta.Id_Cliente, 
                                  venta.Id_Empleado, 
                                  IdProducto))
        self.cursor.commit()
        
    #def ElimiarVenta(self, )