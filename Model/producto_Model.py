from db.Conexion import Conexion 
from Entities.producto import Producto

class ProductoModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()

    def CargarCafes(self):
        sql = 'SELECT Nombre, Descripcion, Precio, Imagen FROM Producto WHERE IdCategoria = 1'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def CargarPostres(self):
        sql = 'SELECT Nombre, Descripcion, Precio, Imagen FROM Producto WHERE IdCategoria = 2'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def CargarBebidasFrias(self):
        sql = 'SELECT Nombre, Descripcion, Precio, Imagen FROM Producto WHERE IdCategoria = 3'
        self.cursor.execute(sql)
        return self.cursor.fetchall()    
    
    def BuscarProducto(self, Idproducto):
        sql = 'SELECT * FROM Producto WHERE IdProducto = ?'
        self.cursor.execute(sql,(Idproducto,))
        return self.cursor.fetchone()
        
    def EliminarProducto(self, Idproducto):
        sql = 'DELETE FROM Producto WHERE IdProducto = ?'
        self.cursor.execute(sql,(Idproducto,))
        self.db.commit()
    
    def GuardarProducto(self, producto: Producto, imagen_path=None):
        sql = 'INSERT INTO Producto (Nombre, Descripcion, Stock, Precio, IdCategoria, IdProveedor, Imagen) VALUES (?, ?, ?, ?, ?, ?, ?)'
        self.cursor.execute(sql, (producto.nombre,
        producto.descripcion,
        producto.stock,
        producto.precio,
        producto.idCategoria,
        producto.idProveedor,
        imagen_path))
        self.db.commit()
    
    def ModificarProducto(self, producto: Producto, Idproducto, imagen_path=None):
        # Si hay imagen nueva, actualizar con ella; si no, mantener la anterior
        if imagen_path:
            sql = 'UPDATE Producto SET Nombre = ?, Descripcion = ?, Stock = ?, Precio = ?, IdCategoria = ?, IdProveedor = ?, Imagen = ? WHERE IdProducto = ? '
            self.cursor.execute(sql, (producto.nombre,
            producto.descripcion,
            producto.stock,
            producto.precio,
            producto.idCategoria,
            producto.idProveedor,
            imagen_path,
            Idproducto))
        else:
            sql = 'UPDATE Producto SET Nombre = ?, Descripcion = ?, Stock = ?, Precio = ?, IdCategoria = ?, IdProveedor = ? WHERE IdProducto = ? '
            self.cursor.execute(sql, (producto.nombre,
            producto.descripcion,
            producto.stock,
            producto.precio,
            producto.idCategoria,
            producto.idProveedor,
            Idproducto))
        self.db.commit()

    def ObtenerCategorias(self):
        sql = 'SELECT IdCategoria, Nombre_Categoria FROM Categoria'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def ObtenerProveedores(self):
        sql = 'SELECT IdProveedor, Nombre FROM Proveedor'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def ObtenerId(self, Nombre):
        sql = 'SELECT IdProducto FROM Producto WHERE Nombre = ?'
        self.cursor.execute(sql, (Nombre,))
        return self.cursor.fetchone()
