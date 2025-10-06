from db.Conexion import Conexion
from Entities.proveedor import Proveedor

class ProveedorModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()
                
    def CargarProveedor(self):
        sql = 'SELECT * FROM Proveedor'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def AgregarProveedor(self, proveedor: Proveedor):
        sql = 'INSERT INTO Proveedor (Nombre, Correo, Telefono) VALUES (?,?,?)'
        self.cursor.execute(sql,(proveedor.nombre, proveedor.correo, proveedor.telefono))
    
    def EliminarProveedor(self, id: int):
        sql = 'DELETE * FROM Proveedor WHERE IdProveedor = ?'
        self.cursor.execute(sql,(id,))
        
    def ModificarProveedor(self, proveedor:Proveedor, id: int ):
        sql = 'UPDATE FROM Proveedor SET Nombre = ?, Correo = ?, Telefono = ? WHERE IdProveedor = ? '
        self.cursor.execute(sql,(proveedor.nombre, proveedor.correo, proveedor.telefono, id))
        