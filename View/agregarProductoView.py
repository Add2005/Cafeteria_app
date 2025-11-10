import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image
import os

# Formulario para agregar producto
def crear_vista_agregar_producto(tab_agregar, paleta, controller, categorias, proveedores):
    COLOR_PRIMARY = paleta['principal']
    COLOR_SECONDARY = paleta['secundario']
    COLOR_TEXT = paleta['texto']
    COLOR_BG_CARD = paleta['tarjeta']
    
    imagen_agregar_path = None

        # PESTAÑA AGREGAR PRODUCTO

    # frame principal 
    ContenedorAgregar = ctk.CTkFrame(tab_agregar, fg_color="transparent")
    ContenedorAgregar.place(relx=0, rely=0, relwidth=1, relheight=1)

    # frame izq con scroll
    FrameAgregarFormulario = ctk.CTkScrollableFrame(ContenedorAgregar, fg_color="transparent", width=500)
    FrameAgregarFormulario.place(relx=0.02, rely=0.02, relwidth=0.62, relheight=0.96)

    # información general: formulario (izq) y la imagen irá a la derecha
    FrameGeneral = ctk.CTkFrame(FrameAgregarFormulario, fg_color=COLOR_PRIMARY, height=420)
    FrameGeneral.pack(fill="x", pady=(0, 10)) 
        # titulo
    lblTituloAgregar = ctk.CTkLabel(FrameGeneral, text="General", font=ctk.CTkFont(size=16, weight="bold"), text_color=COLOR_TEXT)
    lblTituloAgregar.place(x=15, y=50)

        # nombre
    lblNombre = ctk.CTkLabel(FrameGeneral, text="Nombre", font=ctk.CTkFont(12), text_color=COLOR_TEXT)
    lblNombre.place(x=15, y=85)

    etyNombre = ctk.CTkEntry(FrameGeneral, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT, height=35)
    etyNombre.place(x=15, y=110, relwidth=0.92)

        # descripcion
    lblDescripcion = ctk.CTkLabel(FrameGeneral, text="Descripción", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblDescripcion.place(x=15, y=155)

    etyDescripcion = ctk.CTkTextbox(FrameGeneral, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT, height=80, border_width=2)
    etyDescripcion.place(x=15, y=180, relwidth=0.92)

        # precio
    lblPrecio = ctk.CTkLabel(FrameGeneral, text="Precio", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblPrecio.place(x=15, y=270)

    etyPrecio = ctk.CTkEntry(FrameGeneral, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT, height=35)
    etyPrecio.place(x=15, y=295, relwidth=0.92)

            # stock/disponibilidad
    lblStock = ctk.CTkLabel(FrameGeneral, text="Stock", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblStock.place(x=15, y=340)

    etyStock = ctk.CTkEntry(FrameGeneral, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT,
    height=35, placeholder_text="0 (valor actual)")
    etyStock.place(x=15, y=365, relwidth=0.92)


    # FRAME: DETALLES DEL PRODUCTO
    FrameDetalles = ctk.CTkFrame(FrameAgregarFormulario, fg_color=COLOR_PRIMARY, height=215)
    FrameDetalles.pack(fill="x", pady=10) 
    lblDetallesTitulo = ctk.CTkLabel(FrameDetalles, text="Detalles del producto", font=ctk.CTkFont(size=16, weight="bold"), text_color=COLOR_TEXT)
    lblDetallesTitulo.place(x=15, y=15)

        # categoria con combobox - obteniendo categorias de la bd
    
    # categorias = controller.obtener_categorias()
    categorias_dict = {cat[1]: cat[0] for cat in categorias}  # Mapeo nombre a id
    categorias_nombres = list(categorias_dict.keys())
    
    lblCategoria = ctk.CTkLabel(FrameDetalles, text="Categoría", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblCategoria.place(x=15, y=50)

    # si no hay categorias, mostrar mensaje
    etyCategoria = ctk.CTkComboBox(FrameDetalles, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT,
    height=35, state="readonly", button_color=COLOR_SECONDARY, button_hover_color=COLOR_PRIMARY, values=categorias_nombres if categorias_nombres else ["No hay categorías"])

    etyCategoria.place(x=15, y=75, relwidth=0.92)
    if categorias_nombres:
        etyCategoria.set(categorias_nombres[0])  # Seleccionar la primera categoría por defecto
    
    # proveedores con combobox - obteniendo proveedores de la bd
    proveedores_dict = {prov[1]: prov[0] for prov in proveedores}  # Mapeo nombre a id
    proveedores_nombres = list(proveedores_dict.keys())
    
    lblProveedor = ctk.CTkLabel(FrameDetalles, text="Proveedor", font=ctk.CTkFont(size=12), text_color=COLOR_TEXT)
    lblProveedor.place(x=15, y=120)

    etyProveedor = ctk.CTkComboBox(FrameDetalles, fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY, text_color=COLOR_TEXT,
    height=35, state="readonly", button_color=COLOR_SECONDARY, button_hover_color=COLOR_PRIMARY, values=proveedores_nombres if proveedores_nombres else ["No hay proveedores"])
    
    etyProveedor.place(x=15, y=150, relwidth=0.92)
    if proveedores_nombres:
        etyProveedor.set(proveedores_nombres[0])  # Seleccionar el primer proveedor por defecto

    # thumbnail de la imagen del producto (imagen de vista previa)
    FrameThumbnail = ctk.CTkFrame(ContenedorAgregar, fg_color=COLOR_PRIMARY, width=250)
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
    lblHelpImagen.place(relx=0.5, y=340, anchor="n")

    # función para cargar la imagen
    def CargarImagen():
        nonlocal imagen_agregar_path
        file_path = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            try:
                imagen_agregar_path = file_path
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

        # validacion que todos los campos estén llenos
    def ValidarCamposAgregar():
        nombre = etyNombre.get().strip()
        descripcion = etyDescripcion.get("1.0", "end").strip()
        precio = etyPrecio.get().strip()
        stock = etyStock.get().strip()
        categoria_nombre = etyCategoria.get().strip()
        proveedor_nombre = etyProveedor.get().strip()

        if not nombre or not descripcion or not precio or not stock or not categoria_nombre or not proveedor_nombre:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos del formulario.")
            return False
        
        # validar que precio y stock sean numeros
        try:
            precio = float(precio)
            stock = int(stock)
        except ValueError:
            messagebox.showwarning("Datos inválidos", "Por favor, ingrese un valor numérico válido.")
            return False

        # validar que se haya cargado una imagen
        if not imagen_agregar_path:
            messagebox.showwarning("Imagen faltante", "Por favor, cargue una imagen para el producto.")
            return False

        return True
    
        # función para agregar el producto
    def AgregarProducto():
        nonlocal imagen_agregar_path # nonlocal para usar la variable de la funcion padre - muy diferente a global

        valido = ValidarCamposAgregar()
        if not valido:
            return
        try:
            nombre = etyNombre.get().strip()
            descripcion = etyDescripcion.get("1.0", "end").strip()
            precio = float(etyPrecio.get().strip())
            stock = int(etyStock.get().strip())
            categoria_nombre = etyCategoria.get().strip()
            proveedor_nombre = etyProveedor.get().strip()

            # obtener ids de categoria y proveedor
            categoria_nombre = etyCategoria.get()
            categoria_id = categorias_dict[categoria_nombre]
            proveedor_nombre = etyProveedor.get()
            proveedor_id = proveedores_dict[proveedor_nombre]

            # Guardar imagen en la carpeta imgs/productos y obtener ruta relativa
            ruta_imagen = controller.GuardarImagen(imagen_agregar_path)

            # llamar al controlador para agregar el producto con la ruta guardada
            controller.AgregarProducto(nombre, descripcion, precio, stock, categoria_id, proveedor_id, ruta_imagen)

            messagebox.showinfo("Éxito", "Producto agregado exitosamente.")

            # limpiar formulario
            etyNombre.delete(0, 'end')
            etyDescripcion.delete("1.0", "end")
            etyPrecio.delete(0, 'end')
            etyStock.delete(0, 'end')
            if categorias_nombres:
                etyCategoria.set(categorias_nombres[0])
            if proveedores_nombres:
                etyProveedor.set(proveedores_nombres[0])
            imagen_agregar_path = None
            lblPreviewThumbnail.configure(image=imagen_default, text="")  # reset preview
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el producto: {e}")
    
            # botón para agregar producto
    btnAgregarProducto = ctk.CTkButton(FrameAgregarFormulario, text="Agregar producto", fg_color=COLOR_SECONDARY, hover_color=COLOR_PRIMARY, 
        text_color=COLOR_TEXT, height=40, font=ctk.CTkFont(size=14, weight="bold"), command=AgregarProducto, corner_radius=10) 
    btnAgregarProducto.pack(fill="x", pady=20)


# Retornamos los elementos que necesitemos acceder desde la vista principal (no se ocupa)
#     return {
#          'contenedor': ContenedorAgregar,
#          'formulario': FrameAgregarFormulario,
#          'imagen_path': imagen_agregar_path
#      }