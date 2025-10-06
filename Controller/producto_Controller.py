from Model.producto_Model import ProductoModel
from Entities.producto import Producto
#aqui va la vista xd

class ProductoController:
    
    def __init__(self):
        self.model = ProductoModel()
        #inicializar la vista aqui xd

    def ListarProductos(self):
        return self.model.CargarProductos()
        
    def AgregarProducto(self, nombre, desc, stock, precio, idCat, idPro):
        p = Producto(nombre, desc, stock, precio, idCat, idPro)
        self.model.GuardarProducto(p)
        
    def ModificarProducto(self, idproducto, nombre, desc, stock, precio, idCat, idPro):
        p = Producto(nombre, desc, stock, precio, idCat, idPro)
        self.model.ModificarProducto(p, idproducto)
        
    def EliminarProducto(self, idproducto):
        self.model.EliminarProducto(idproducto)
        
        