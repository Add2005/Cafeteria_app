
class detalle_venta:
    
    def __init__(self, IdProducto, Cantidad, IdVenta: int = None):
        self.IdVenta = IdVenta
        self.IdProducto = IdProducto
        self.Cantidad = Cantidad
        
    def transformar_a_tupla(self):
        return (self.IdVenta, self.IdProducto, self.Cantidad)