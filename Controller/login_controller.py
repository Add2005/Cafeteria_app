from Model.usuario_model import usuarioModel

class LoginController:
    
    def __init__(self):
        self.model = usuarioModel()
        
    #obtenemos el rol de la persona que se loguee    
    def Usuario_Accesado(self, nombre):
        return self.model.ObtenerUsuario(nombre)
    
    #verificamos las credenciales ingresadas en la vista
    def on_login(self, nombre_usuario: str, contrasena: str):
        return self.model.verificar_credenciales(nombre_usuario, contrasena)
    
    def RegistrarIdEmpleado(self, Nombre):
        return self.model.BuscarEmpleado(Nombre)
         