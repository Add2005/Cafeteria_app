import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
# from Controller.Producto_Controller import ProductoController

# Vista para modificar y agregar productos
def crear_vista_producto(parent_frame, paleta):

    # controller = ProductoController() llamar al conteolador

    COLOR_PRIMARY = paleta['principal']
    COLOR_SECONDARY = paleta['secundario']
    COLOR_TEXT = paleta['texto']
    COLOR_BG_CARD = paleta['tarjeta']
    COLOR_SUCCESS = "#4CAF50" # agregar el rojo

    # almacenar imagen seleccionada

    ruta_imagen_seleccionada = {"ruta": None} # se usa para cargar la imagen
    # Frame Principal 
    ProductosFrame = ctk.CTkFrame(parent_frame, fg_color=COLOR_PRIMARY)
    ProductosFrame.place(relx=0, rely=1, relwidth=1, relheight=1) # rel: posicionar widgets de forma relativa al tamaño del frame

    lbltitulo = ctk.CTkLabel(ProductosFrame, text="Agregar nuevo producto",
                            font=ctk.CTkFont(size=24, weight="bold"), text_color=COLOR_TEXT
                            text_color=COLOR_TEXT)
    lbltitulo.place(x=20, y=20)

    # Pestañas para Agregar y Modificar
    tabPestañas = ctk.CTkTabview(ProductosFrame, fg_color=COLOR_BG_CARD,
                                 segmented_button_fg_color=COLOR_PRIMARY,
                                 segmented_button_selected_color=COLOR_SECONDARY,
                                 segmented_button_unselected_hover_color=COLOR_SECONDARY, #?
                                 text_color=COLOR_TEXT)
    tabPestañas.place(x=20, y=70, relwidth=0.96, relheight=0.88)

    # Creamos pestañas (agregar y modificar)
    tabAgregar = tabPestañas.add("Agregar producto")
    tabModificar = tabPestañas.add("Modificar producto")

    # VALIDACIONES 

    # esta funcion valida que los datos agregados no estén vacíos y sean correctos
    def ValidarErrores():
        errores = [] # almcenamos los errores para acumularlos y que el usuario los corrija todos de una sola vez

        # obtenemos valores
        nombre = EtyNombre.get().strip()
        precio = EtyPrecio.get().strip()
        stock = EtyStock.get().strip()

    # validación: campos incompletos
        if not nombre or not precio or not stock and not stock.isdigit():
            errores.append("Campos incompletos")
    
        # validación de precio
        if precio:
            try:
                precio_float = float(precio.replace("$", "").replace(",", ""))
                if precio_float <= 0:
                    errores.append("El precio debe ser mayor a 0.00")
            except ValueError:
                errores.append("El precio debe ser un número válido")
        return errores

    def MostrarErrores(errores):
        # mostramos todos los errores en un messagebox
        if errores:
            mensaje_error = "Corrija los siguientes errores:\n\n" + "\n".join(errores)
            messagebox.showerror("Errores", mensaje_error)
            return False
        return True

    # Carga de imagen
    # abre dialogo para colocarle una imagen al producto
    def CargarImagen():
        typearchivo = [
            ("Imágenes", "*.png", "*.jpg", "*.jpeg", "*.bmp"),
            ("PNG", "*.png"),
            ("JPEG", "*.jpg", "*.jpeg"),
            ("Todos los archivos", "*.*")]

        ruta = filedialog.askopenfilename(
        title="Seleccionar imagen del producto",
        filetypes=typearchivo)
        if ruta:
            try:
                # imagen valida
                img = Image.open(ruta)
                # guardamos ruta
                ruta_imagen_seleccionada["ruta"] = ruta

                img_preview = img.copy()  
                # ajustamos la imagen (tamaño) con thumbnail y con resampling cambiamos la rwsolucion 
                # LANCZOS es para mejorar la calidad
                img_preview.thumbnail((210, 150), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img_preview)

                lblimgplaceholder.configure(image=photo, text="")
                lblimgplaceholder.image = photo # mantenemos ref

                BtnCargarImagen.configure(text="Cambiar imagen")

            except Exception as ex:
                messagebox.showerror("Error", f"No se puedo cargar la imagen: {ex}")
                ruta_imagen_seleccionada["ruta"] = None
            

    # Pestaña agregar productos

# frame del form (izq) labels y entrys
    FormFrame = ctk.CTkFrame(tabAgregar, fg_color=COLOR_PRIMARY)
    FormFrame.place(x=10, y=10, relwidth=0.48, relheight=0.96)


    lblformtitulo = ctk.CTkLabel(FormFrame, text="Información del producto",
                                 font=ctk.CTkFont(size=14), text_color=COLOR_TEXT)
    lblformtitulo.place(x=20, y=20)

    lblNombre = ctk.CTkLabel(FormFrame, text="Nombre", font=ctk.CTkFont(size=14), text_color=COLOR_TEXT)
    lblNombre. # y 80 x 20
    EtyNombre = ctk.CTkEntry(FormFrame, )
    # crear entrys y labels para precio y stock y descripcion con textbox, categoria con un combobox?? revisar si hay q poner categoria
    # colocar boton de imagen, hacer disponibilidad con un switch
    # colocar botones de agregar y modificar 

    def AgregarProducto():
        errores = ValidarCamposagregar # funcion que ya se realizo i guess
        if not MostrarErrores(errores):
            return  
    try:
        # obtener valores
        nombre =
        descripcion = EtyDescripccion.get("1.0", "end-1c").strip()

    
    # funcion de limpiar form
    # boton de agregar y limpiar

    






