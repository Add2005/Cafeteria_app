from db.Conexion import Conexion 
from Entities.producto import Producto

class ProductoModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor

    def CargarProductos(self):
        sql = 'SELECT * FROM Producto'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def BuscarProducto(self, Id_producto: int):
        sql = 'SELECT * FROM Producto WHERE Id_Producto = '
        self.cursor.execute(sql,(Id_producto,))
        return self.cursor.fetchone()
    
        
    def EliminarProducto(self, Id_producto: int):
        sql = 'DELETE * FROM Producto WHERE Id_Producto = ?'
        self.cursor.execute(sql,(Id_producto,))
        self.db.Commit()
    
    def GuardarProducto(self, producto: Producto):
        sql = 'INSERT INTO Producto (Nombre, Precio, Stock) VALUES (?,?,?)'
        self.cursor.execute(sql, (producto.nombre, producto.precio, producto.stock))
        self.db.Commit()
    
    def ModificarProducto(self, producto: Producto, Id_producto: int):
        sql = 'UPDATE FROM Producto SET Nombre = ?, Precio = ?, Stock = ? WHERE Id_Producto = -? '
        self.cursor.execute(sql, (producto.nombre, producto.precio, producto.stock, Id_producto))
        self.db.Commit()
    