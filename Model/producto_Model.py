from db.Conexion import Conexion 
from Entities.producto import Producto

class ProductoModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()

    def CargarProductos(self):
        sql = 'SELECT * FROM Producto'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def BuscarProducto(self, Idproducto: int):
        sql = 'SELECT * FROM Producto WHERE Id_Producto = ?'
        self.cursor.execute(sql,(Idproducto,))
        return self.cursor.fetchone()
        
    def EliminarProducto(self, Idproducto: int):
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
    
    def ModificarProducto(self, producto: Producto, Idproducto: int):
        sql = 'UPDATE Producto SET Nombre = ?, Descripcion = ?, Stock = ?, Precio = ?, IdCategoria = ?, IdProveedor = ? WHERE IdProducto = ? '
        self.cursor.execute(sql, (producto.nombre,
        producto.descripcion,
        producto.stock,
        producto.precio,
        producto.idCategoria,
        producto.idProveedor,
        Idproducto))
        self.db.commit()
        