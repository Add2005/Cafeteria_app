class usuario:
    
    sesion_actual = ""
    
    def __init__(self, id_usuario, nombre_usuario, contrasena, rol):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol
    
    #classmethod en este caso nos ayuda a gestior un estado "global" de la sesion actual
    #para la clase usuario :D 
    @classmethod
    def GuardarIdEmpleado(cls, user):
        cls.sesion_actual = user[0]
         
    @classmethod
    def OlvidarIdEmpleado(cls):
        cls.sesion_actual = None
        
        
        