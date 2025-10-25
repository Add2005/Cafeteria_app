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
            return usuario(row.IdUsuario, row.NombreUsuario, row.Contrasena, row.IdRol)
        else:
            return None
        
    def get_user_by_rol(self, rol: int):
        sql = 'SELECT * FROM Usuarios WHERE IdRol = ?'
        self.cursor.execute(sql, (rol,))
        rows = self.cursor.fetchall()
        usuarios = []
        for row in rows:
            usuarios.append(usuario(row.IdUsuario, row.NombreUsuario, row.Contrasena, row.IdRol))
        return usuarios
    
    def crear_usuario(self, usuario: usuario):
        sql = 'INSERT INTO Usuario (NombreUsuario, Contrasena, IdRol) VALUES (?, ?, ?)'
        self.cursor.execute(sql, (usuario.nombre_usuario, usuario.contrasena, usuario.rol))
        self.db.commit()
        