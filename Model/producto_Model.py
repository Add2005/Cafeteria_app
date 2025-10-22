from db.Conexion import Conexion 
from Entities.producto import Producto

class ProductoModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()

    def CargarCafes(self):
        sql = 'SELECT Nombre, Descripcion, Precio FROM Producto WHERE IdCategoria = 1'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def CargarPostres(self):
        sql = 'SELECT Nombre, Descripcion, Precio FROM Producto WHERE IdCategoria = 2'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def CargarBebidasFrias(self):
        sql = 'SELECT Nombre, Descripcion, Precio FROM Producto WHERE IdCategoria = 3'
        self.cursor.execute(sql)
        return self.cursor.fetchall()    
    
    def BuscarProducto(self, Idproducto):
        sql = 'SELECT * FROM Producto WHERE Id_Producto = ?'
        self.cursor.execute(sql,(Idproducto,))
        return self.cursor.fetchone()
        
    def EliminarProducto(self, Idproducto):
        sql = 'DELETE FROM Producto WHERE Id_Producto = ?'
        self.cursor.execute(sql,(Idproducto,))
        self.db.commit()
    
    def GuardarProducto(self, producto: Producto):
        sql = 'INSERT INTO Producto (Nombre, Descripcion, Stock, Precio, IdCategoria, IdProveedor) VALUES (?, ?, ?, ?, ?, ?)'
        self.cursor.execute(sql, (producto.nombre,
        producto.descripcion,
        producto.stock,
        producto.precio,
        producto.idCategoria,
        producto.idProveedor))
        self.db.commit()
    
    def ModificarProducto(self, producto: Producto, Idproducto):
        sql = 'UPDATE Producto SET Nombre = ?, Descripcion = ?, Stock = ?, Precio = ?, IdCategoria = ?, IdProveedor = ? WHERE IdProducto = ? '
        self.cursor.execute(sql, (producto.nombre,
        producto.descripcion,
        producto.stock,
        producto.precio,
        producto.idCategoria,
        producto.idProveedor,
        Idproducto))
        self.db.commit()
        