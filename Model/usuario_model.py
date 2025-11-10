from db.Conexion import Conexion
from Entities.usuario import usuario

class usuarioModel:
    
    def __init__(self):
        self.db = Conexion()
        self.cursor = self.db.cursor()
        
    def verificar_credenciales(self, nombre_usuario: str, contrasena: str):
        sql = 'SELECT * FROM Usuarios WHERE NombreUsuario = ? AND Contrasena = ?'
        self.cursor.execute(sql, (nombre_usuario, contrasena))
        row = self.cursor.fetchone()
        if row:
            return True
        else:
            return False

    def ObtenerUsuario(self, nombre):
        sql = 'SELECT * FROM Usuarios WHERE NombreUsuario = ?'
        self.cursor.execute(sql, (nombre,))
        row = self.cursor.fetchone()
        return usuario(row.IdUsuario, row.NombreUsuario, row.Contrasena, row.IdRol)

    def crear_usuario(self, usuario: usuario):
        sql = 'INSERT INTO Usuario (NombreUsuario, Contrasena, IdRol) VALUES (?, ?, ?)'
        self.cursor.execute(sql, (usuario.nombre_usuario, usuario.contrasena, usuario.rol))
        self.db.commit()
        
    def BuscarEmpleado(self, Nombre):
        sql = 'SELECT IdEmpleado FROM Usuarios WHERE NombreUsuario = ?'
        self.cursor.execute(sql,(Nombre,))
        return self.cursor.fetchone()