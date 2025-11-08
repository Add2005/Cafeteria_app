import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image
import os

# Modificar y eliminar productos
def crear_vista_modificar_producto(TabModificar, paleta, controller, categorias, proveedores):
    COLOR_PRIMARY = paleta['principal']
    COLOR_SECONDARY = paleta['secundario']
    COLOR_TEXT = paleta['texto']
    COLOR_BG_CARD = paleta['tarjeta']
    
    imagen_modificar_path = None

        # contenedor modificar
    ContenedorModificar = ctk.CTkFrame(TabModificar, fg_color="transparent")
    ContenedorModificar.place(relx=0, rely=0, relwidth=1, relheight=1)

    
    FrameModificarFormulario = ctk.CTkScrollableFrame(ContenedorModificar, fg_color="transparent", width=500)
    FrameModificarFormulario.place(relx=0.02, rely=0.02, relwidth=0.62, relheight=0.96)

    # Buscar producto (frame, lbl, entry)
    FrameBuscarProducto = ctk.CTkFrame(FrameModificarFormulario, fg_color=COLOR_PRIMARY, height=125)
    FrameBuscarProducto.pack(fill="x", pady=(0, 10))
    
        # títulos, labels y entrys
    lblBuscarTitulo = ctk.CTkLabel(FrameBuscarProducto, text="Buscar producto", font=ctk.CTkFont(size=16, weight="bold"), text_color=COLOR_TEXT)
    lblBuscarTitulo.place(x=15, y=15)

    lblIdProducto = ctk.CTkLabel(FrameBuscarProducto, text="ID del producto", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblIdProducto.place(x=15, y=50)

    EtyIDProducto = ctk.CTkEntry(FrameBuscarProducto, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY,
    text_color=COLOR_TEXT, height=35, width=300, placeholder_text="Ingrese el ID del producto")

    EtyIDProducto.place(x=15, y=75, relwidth=0.65)

    # Info general
    FrameGeneral = ctk.CTkFrame(FrameModificarFormulario, fg_color=COLOR_PRIMARY, height=380)
    FrameGeneral.pack(fill="x", pady=10) 

    lblTituloModificar = ctk.CTkLabel(FrameGeneral, text="General", font=ctk.CTkFont(size=16, weight="bold"), text_color=COLOR_TEXT)
    lblTituloModificar.place(x=15, y=15)

    lblNombre = ctk.CTkLabel(FrameGeneral, text="Nombre del producto", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblNombre.place(x=15, y=50)

    etyNombre = ctk.CTkEntry(FrameGeneral, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT, height=35)
    etyNombre.place(x=15, y=75, relwidth=0.92)

        # descripcion
    lblDescripcion = ctk.CTkLabel(FrameGeneral, text="Descripción", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblDescripcion.place(x=15, y=120)

    etyDescripcion = ctk.CTkTextbox(FrameGeneral, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT, height=80, border_width=2)
    etyDescripcion.place(x=15, y=145, relwidth=0.92)

        # precio
    lblPrecio = ctk.CTkLabel(FrameGeneral, text="Precio", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblPrecio.place(x=15, y=235)

    etyPrecio = ctk.CTkEntry(FrameGeneral, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT, height=35)
    etyPrecio.place(x=15, y=260, relwidth=0.92)

            # stock/disponibilidad
    lblStock = ctk.CTkLabel(FrameGeneral, text="Stock", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblStock.place(x=15, y=305)

    etyStock = ctk.CTkEntry(FrameGeneral, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT, height=35, placeholder_text="0 (valor actual)")
    etyStock.place(x=15, y=330, relwidth=0.92)

    # FRAME: DETALLES DEL PRODUCTO
    FrameDetalles = ctk.CTkFrame(FrameModificarFormulario, fg_color=COLOR_PRIMARY, height=265)
    FrameDetalles.pack(fill="x", pady=10)

    lblDetallesTitulo = ctk.CTkLabel(FrameDetalles, text="Detalles del producto", font=ctk.CTkFont(size=16, weight="bold"), text_color=COLOR_TEXT)
    lblDetallesTitulo.place(x=15, y=15)
    
    # categoria
    categorias_dict = {cat[1]: cat[0] for cat in categorias}  # Mapeo nombre a id
    categorias_nombres = list(categorias_dict.keys())
    
    lblCategoria = ctk.CTkLabel(FrameDetalles, text="Categoría", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblCategoria.place(x=15, y=50)

    etyCategoria = ctk.CTkComboBox(FrameDetalles, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT,
    height=35, state="readonly", button_color=COLOR_SECONDARY, button_hover_color=COLOR_PRIMARY, values=categorias_nombres if categorias_nombres else ["No hay categorías"])
    
    etyCategoria.place(x=15, y=75, relwidth=0.92)
    if categorias_nombres:
        etyCategoria.set(categorias_nombres[0])  # Seleccionar la primera categoría por defecto

    # proveedor
    proveedores_dict = {prov[1]: prov[0] for prov in proveedores}  # Mapeo nombre a id
    proveedores_nombres = list(proveedores_dict.keys())
    
    lblProveedor = ctk.CTkLabel(FrameDetalles, text="Proveedor", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblProveedor.place(x=15, y=120)

    etyProveedor = ctk.CTkComboBox(FrameDetalles, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT,
    height=35, state="readonly", button_color=COLOR_SECONDARY, button_hover_color=COLOR_PRIMARY, values=proveedores_nombres if proveedores_nombres else ["No hay proveedores"])
    
    etyProveedor.place(x=15, y=150, relwidth=0.92)
    if proveedores_nombres:
        etyProveedor.set(proveedores_nombres[0])  # Seleccionar el primer proveedor por defecto

    # validación de campos
    def ValidarCamposModificar():
        id_producto = EtyIDProducto.get().strip()
        nombre = etyNombre.get().strip()
        descripcion = etyDescripcion.get("1.0", "end").strip()
        precio = etyPrecio.get().strip()
        stock = etyStock.get().strip()

        if not id_producto.isdigit():
            messagebox.showwarning("ID inválido", "Por favor, ingrese un ID de producto válido (número entero).")
            return False

        if not id_producto or not nombre or not descripcion or not precio or not stock:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos del formulario.")
            return False
        
        # validar que precio y stock sean numeros
        try:
            precio = float(precio)
            stock = int(stock)
        except ValueError:
            messagebox.showwarning("Datos inválidos", "Por favor, ingrese un valor numérico válido.")
            return False
        return True

    def ModificarProducto():
        valido = ValidarCamposModificar()
        if not valido:
            return
        try:
            id_producto = EtyIDProducto.get().strip()
            nombre = etyNombre.get().strip()
            descripcion = etyDescripcion.get("1.0", "end").strip()
            precio = float(etyPrecio.get().strip())
            stock = int(etyStock.get().strip())
            categoria_nombre = etyCategoria.get().strip()
            proveedor_nombre = etyProveedor.get().strip()

            # obtener ids de categoria y proveedor
            categoria_id = categorias_dict[categoria_nombre]
            proveedor_id = proveedores_dict[proveedor_nombre]

            actualizado = controller.ModificarProducto(id_producto, nombre, descripcion, stock, precio)
            if actualizado:
                messagebox.showinfo("Éxito", f"Producto '{nombre}' modificado correctamente.")
                # Limpiar campos después de modificar
                EtyIDProducto.delete(0, 'end')
                etyNombre.delete(0, 'end')
                etyDescripcion.delete("1.0", "end")
                etyPrecio.delete(0, 'end')
                etyStock.delete(0, 'end')
                if categorias_nombres:
                    etyCategoria.set(categorias_nombres[0])
                if proveedores_nombres:
                    etyProveedor.set(proveedores_nombres[0])
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar el producto: {e}")

    # Botón modificar
    btnModificarProducto = ctk.CTkButton(FrameDetalles, text="Modificar producto", fg_color=COLOR_SECONDARY,
    hover_color=COLOR_PRIMARY, text_color=COLOR_TEXT, height=40, font=ctk.CTkFont(size=14, weight="bold"), command=ModificarProducto)
    btnModificarProducto.place(x=15, y=210, relwidth=0.92)

    # THUMBNAIL
    # thumbnail de la imagen del producto (imagen de vista previa)
    FrameThumbnail = ctk.CTkFrame(ContenedorModificar, fg_color=COLOR_PRIMARY, width=250)
    FrameThumbnail.place(relx=0.66, rely=0.02, relwidth=0.32, relheight=0.96)

    lblThumbnailTitulo = ctk.CTkLabel(FrameThumbnail, text="Imagen del producto", font=ctk.CTkFont(size=14, weight="bold"), text_color=COLOR_TEXT)
    lblThumbnailTitulo.place(x=15, y=15)
    # frame para la imagen
    FrameImagenProducto = ctk.CTkFrame(FrameThumbnail, fg_color=COLOR_BG_CARD, width=200, height=200) 
    FrameImagenProducto.place(relx=0.5, y=50, anchor="n")
    # cargar imagen para el preview del thumbnail
    imagen_default = ctk.CTkImage(Image.open("imgs/upload.png").resize((200, 220)), size=(200, 220))

    # icono de imagen por defecto
    lblPreviewThumbnail = ctk.CTkLabel(FrameImagenProducto, image=imagen_default, text="", text_color=COLOR_TEXT, fg_color="transparent") 
    lblPreviewThumbnail.place(relx=0.5, rely=0.5, anchor="center")

    # texto de ayuda para subir imagen
    lblHelpImagen = ctk.CTkLabel(FrameThumbnail, text="Seleccione una imagen para el producto", font=ctk.CTkFont(size=10), text_color=COLOR_TEXT, justify="center")
    lblHelpImagen.place(relx=0.5, y=340, anchor="n") # 5px debajo del botón

    # función para cargar la imagen
    def CargarImagen():
        nonlocal imagen_modificar_path
        file_path = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            try:
                imagen_modificar_path = file_path
                img = Image.open(file_path)
                img.thumbnail((200, 200), Image.Resampling.LANCZOS)
                photo = ctk.CTkImage(light_image=img, dark_image=img, size=(200, 200))

                # actualizar preview
                lblPreviewThumbnail.configure(image=photo, text="")
                lblPreviewThumbnail.image = photo  # mantener referencia
                lblPreviewThumbnail.configure(text=os.path.basename(file_path))  # mostrar nombre del archivo debajo de la imagen
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
        # botón para cargar imagen
    btnCargarImagen = ctk.CTkButton(FrameThumbnail, text="Cargar Imagen", fg_color=COLOR_SECONDARY, hover_color=COLOR_PRIMARY,
    text_color=COLOR_TEXT, height=35, command=CargarImagen, width=200)
    btnCargarImagen.place(relx=0.5, y=280, anchor="n")

    # Función para buscar el producto
    def BuscarProducto():
        nonlocal imagen_modificar_path
        try:
            id_producto = EtyIDProducto.get().strip()
            if not id_producto:
                messagebox.showwarning("ID vacío", "Por favor, ingrese un ID de producto.")
                return
            if not id_producto.isdigit():
                messagebox.showwarning("ID inválido", "Por favor, ingrese un ID de producto válido (número entero).")
                return
            
            producto = controller.BuscarProducto(id_producto)
            if producto:
                # llenar los campos con la info del producto
                etyNombre.delete(0, 'end')
                etyNombre.insert(0, producto[1])

                etyDescripcion.delete("1.0", "end")
                etyDescripcion.insert("1.0", producto[2])

                etyStock.delete(0, 'end')
                etyStock.insert(0, str(producto[3]))

                etyPrecio.delete(0, 'end')
                etyPrecio.insert(0, f"{producto[4]:.2f}")

                # buscar nombre de la categoria y proveedor
                categoria_encontrada = next((cat[1] for cat in categorias if cat[0] == producto[5]), None)
                if categoria_encontrada:
                    etyCategoria.set(categoria_encontrada)
                            
                proveedor_encontrado = next((prov[1] for prov in proveedores if prov[0] == producto[6]), None)
                if proveedor_encontrado:
                    etyProveedor.set(proveedor_encontrado)
                messagebox.showinfo("Producto encontrado", f"Producto '{producto[1]}' cargado para modificar.")
            else:
                messagebox.showwarning("No encontrado", "No se encontró ningún producto con ese ID.")
        except ValueError:
            messagebox.showwarning("ID inválido", "Por favor, ingrese un ID de producto válido (número entero).")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el producto: {e}")
    
    lupa = ctk.CTkImage(Image.open("imgs/lupa.png"), size=(15, 15))
    btnBuscarProducto = ctk.CTkButton(FrameBuscarProducto, image=lupa, text="", fg_color=COLOR_SECONDARY, hover_color=COLOR_PRIMARY,
    text_color=COLOR_TEXT, height=35, command=BuscarProducto)

    btnBuscarProducto.place(relx=0.72, y=75, relwidth=0.12)

    # Retornamos los elementos que necesitemos acceder desde la vista principal
    return {
        'imagen_path': imagen_modificar_path
    }