from db.Conexion import Conexion
from Entities.proveedor import Proveedor

class ProveedorModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()
                
    def CargarProveedores(self):
        sql = 'SELECT * FROM Proveedor'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def GuardarProveedor(self, proveedor: Proveedor):
        sql = 'INSERT INTO Proveedor (Nombre, Correo, Telefono) VALUES (?,?,?)'
        self.cursor.execute(sql,(proveedor.nombre, 
                                 proveedor.correo, 
                                 proveedor.telefono))
    
    def EliminarProveedor(self, id):
        sql = 'DELETE * FROM Proveedor WHERE IdProveedor = ?'
        self.cursor.execute(sql,(id,))
        
    def ModificarProveedor(self, proveedor:Proveedor, id):
        sql = 'UPDATE FROM Proveedor SET Nombre = ?, Correo = ?, Telefono = ? WHERE IdProveedor = ? '
        self.cursor.execute(sql,(proveedor.nombre, 
                                 proveedor.correo, 
                                 proveedor.telefono, 
                                 id))
        
    def BuscarProvedor(self, idproveedor):
        sql = 'SELECT * FROM Proveedor WHERE IdProveedor = ?'
        self.cursor.execute(sql, (idproveedor,))
        return self.cursor.fetchone()
        