import customtkinter as ctk
from Controller.producto_Controller import ProductoController
from .agregarProductoView import crear_vista_agregar_producto
from .modificarProductoView import crear_vista_modificar_producto

def crear_vista_producto(parent_frame, paleta):

    controller = ProductoController()

    COLOR_PRIMARY = paleta['principal']
    COLOR_SECONDARY = paleta['secundario']
    COLOR_TEXT = paleta['texto']
    COLOR_BG_CARD = paleta['tarjeta']
    
    # FRAME PRINCIPAL
    ProductoFrame = ctk.CTkFrame(parent_frame, fg_color=COLOR_PRIMARY)
    ProductoFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

    ctk.CTkLabel(ProductoFrame, text="Gestión de Productos", font=ctk.CTkFont(size=24, weight="bold"),
                 text_color=COLOR_TEXT, bg_color=COLOR_PRIMARY).place(x=20, y=20)

    # tab view para agregar y modificar productos
    tabview = ctk.CTkTabview(ProductoFrame, fg_color=COLOR_BG_CARD,
                             segmented_button_fg_color=COLOR_SECONDARY,
                             segmented_button_selected_color=COLOR_SECONDARY,
                             segmented_button_selected_hover_color=COLOR_PRIMARY,
                             text_color=COLOR_TEXT)
    tabview.place(relx=0.02, rely=0.10, relwidth=0.96, relheight=0.88)


    # Creamos pestañas agregar y modificar
    tabview.add("Agregar")
    tabview.add("Modificar")

    # cargar categorias y proveedores
    categorias = controller.ListarCategorias()
    proveedores = controller.ListarProveedores()

    TabAgregar = tabview.tab("Agregar")
    crear_vista_agregar_producto(TabAgregar, paleta, controller, categorias, proveedores)

    TabModificar = tabview.tab("Modificar")
    crear_vista_modificar_producto(TabModificar, paleta, controller, categorias, proveedores)

    return ProductoFrame
