from Model.proveedor_Model import ProveedorModel 
from Entities.proveedor import Proveedor

class ProveedorController:
    
    def __init__(self):
        self.model = ProveedorModel()
        
    def ListarProveedor(self):
        return self.model.CargarProveedores()
    
    def AgregarProveedor(self, nombre, correo, telefono):
        p = Proveedor(nombre, correo, telefono)
        self.model.GuardarProveedor(p)
        
    def ModificarProveedor(self, nombre, correo, telefono, IdProveedor):
        p = Proveedor(nombre, correo, telefono)
        self.model.ModificarProveedor(p, IdProveedor)
        
    def EliminarProveedor(self, IdProveedor):
        self.model.EliminarProveedor(IdProveedor)
        
    def BuscarProveedor(self, IdProveedor):
        return self.BuscarProveedor(IdProveedor)
        
        
    
        

