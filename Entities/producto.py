class Producto:

    def __init__(self,nombre, cantidad, precio, descripcion, stock):
        if precio < 0:
            raise ValueError('El precio no puede ser negativo')
        if stock < 0:
            raise ValueError('El stock no puede ser negativo')
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock
        
