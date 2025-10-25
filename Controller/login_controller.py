from Model.usuario_model import usuarioModel
from View.login import LoginView
from View.dashboard import run_dashboard


class LoginController:
    def __init__(self):
        #el model se instancia para verificar credenciales
        self.model = usuarioModel()
        #la vista se instancia y se le pasa el controller
        self.view = LoginView(controller=self)

    def mostrar(self):
        self.view.mostrar()
        
    #obtenemos los usuarios con cierto rol    
    def perimisos_acceso(self, rol: int):
        usuarios = self.model.get_user_by_rol(rol)
        return usuarios
    
    #verificamos las credenciales ingresadas en la vista
    def on_login(self, nombre_usuario: str, contrasena: str):
        user = self.model.verificar_credenciales(nombre_usuario, contrasena)
        if user:
            self.view.mostrar_mensaje(f"Bienvenido {user.nombre_usuario}")
            self.view.cerrar()
            run_dashboard(user)
        else:
            self.view.mostrar_mensaje("Usuario o contraseña incorrectos", tipo="error")
    
    
            
    
        