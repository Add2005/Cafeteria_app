import re
pEmail = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
pTel = r"^\d{4}-\d{4}$"

class Proveedor:
    
    def __init__(self, id, nombre, correo: str, telefono: str):
        self.id = id
        if re.match(pEmail, correo):
            self.correo = correo
        else:
            raise ValueError
        if re.match(pTel, telefono):
            self.telefono = telefono
        else:
            raise ValueError
        self.nombre = nombre    
        