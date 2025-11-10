from Model.producto_Model import ProductoModel
from Entities.producto import Producto
import shutil
import os
from pathlib import Path

class ProductoController:
    
    def __init__(self):
        self.model = ProductoModel()
        # Crear carpeta de productos si no existe
        self.productos_dir = Path("imgs/productos")
        self.productos_dir.mkdir(parents=True, exist_ok=True)

    def ListarCafes(self):
        return self.model.CargarCafes()
        
    def ListarPostres(self):
        return self.model.CargarPostres()
            
    def ListarBebidasFrias(self):
        return self.model.CargarBebidasFrias()
        
    def AgregarProducto(self, nombre, desc, stock, precio, idCat, idPro, imagen_path):
        p = Producto(None, nombre, desc, stock, precio, idCat, idPro, imagen_path)
        self.model.GuardarProducto(p, imagen_path)
        return True
        
    def ModificarProducto(self, idproducto, nombre, desc, stock, precio, idCat, idProveedor, imagen_path=None):
        # Crear entidad Producto con id=None (el id se pasa aparte) y pasar imagen_path al atributo correcto
        p = Producto(None, nombre, desc, stock, precio, idCat, idProveedor, imagen_path)
        self.model.ModificarProducto(p, idproducto, imagen_path)
        return True
        
    def EliminarProducto(self, idproducto):
        self.model.EliminarProducto(idproducto)
        
    def BuscarProducto(self, idproducto):
        return self.model.BuscarProducto(idproducto)

    def ListarCategorias(self):
        return self.model.ObtenerCategorias()

    def ListarProveedores(self):
        return self.model.ObtenerProveedores()
    
    def ObtenerId(self, Nombre):
        return self.model.ObtenerId(Nombre)
    
    def GuardarImagen(self, archivo_path):
        if not archivo_path or not os.path.exists(archivo_path):
            raise ValueError("El archivo de imagen no existe")
        
        try:
            # Obtener nombre del archivo
            nombre_archivo = os.path.basename(archivo_path)
            
            # Ruta destino
            ruta_destino = self.productos_dir / nombre_archivo
            
            # Si el archivo ya existe, agregar timestamp para evitar conflictos
            if ruta_destino.exists():
                nombre_base, extension = os.path.splitext(nombre_archivo)
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                nombre_archivo = f"{nombre_base}_{timestamp}{extension}"
                ruta_destino = self.productos_dir / nombre_archivo
            
            # Copiar archivo
            shutil.copy2(archivo_path, ruta_destino)
            
            # Retornar ruta relativa para guardar en BD
            ruta_relativa = str(ruta_destino).replace("\\", "/")
            return ruta_relativa
            
        except Exception as e:
            raise Exception(f"Error al guardar la imagen: {e}")