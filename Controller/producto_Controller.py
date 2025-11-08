from Model.producto_Model import ProductoModel
from Entities.producto import Producto

class ProductoController:
    
    def __init__(self):
        self.model = ProductoModel()

    def ListarCafes(self):
        return self.model.CargarCafes()
        
    def ListarPostres(self):
        return self.model.CargarPostres()
            
    def ListarBebidasFrias(self):
        return self.model.CargarBebidasFrias()
        
    def AgregarProducto(self, nombre, desc, stock, precio, idCat, idPro):
        p = Producto(nombre, desc, stock, precio, idCat, idPro)
        self.model.GuardarProducto(p)
        
    def ModificarProducto(self, idproducto, nombre, desc, stock, precio, idCat, idProveedor):
        p = Producto(nombre, desc, stock, precio, idCat, idProveedor)
        self.model.ModificarProducto(p, idproducto)
        
    def EliminarProducto(self, idproducto):
        self.model.EliminarProducto(idproducto)
        
    def BuscarProducto(self, idproducto):
        return self.model.BuscarProducto(idproducto)
    # En Producto_Controller.py - agregar estos métodos

    def ListarCategorias(self):
        return self.model.ObtenerCategorias()

    def ListarProveedores(self):
        return self.model.ObtenerProveedores()