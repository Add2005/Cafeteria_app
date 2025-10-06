#Entidad producto
class Producto:

    def __init__(self, nombre, descripcion, stock, precio, idCategoria, idProveedor ):
        if precio < 0:
            raise ValueError('El precio no puede ser negativo')
        if stock < 0:
            raise ValueError('El stock no puede ser negativo')
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock
        self.idCategoria = idCategoria
        self.idProveedor = idProveedor
        
        
