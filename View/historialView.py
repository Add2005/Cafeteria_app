import customtkinter as ctk
from tkinter import ttk  # Usamos ttk para el Treeview que se parece a una tabla
from Controller.orden_Controller import obtener_historial_ordenes

# ------ REGISTRO/HISTORIAL DE VENTAS ------
def crear_vista_historial(parent_frame, paleta):
    
    # Definición de Colores 
    COLOR_PRIMARY = paleta['principal']
    COLOR_SECONDARY = paleta['secundario']
    COLOR_TEXT = paleta['texto']
    COLOR_BG_CARD = paleta['tarjeta']

    #  Frame Principal de la Vista 
    historial_frame = ctk.CTkFrame(parent_frame, fg_color=COLOR_PRIMARY)
    historial_frame.grid_columnconfigure(0, weight=1)
    historial_frame.grid_rowconfigure(3, weight=1) # Fila para la tabla

    # Título de la Vista 
    title_label = ctk.CTkLabel(historial_frame, text="Órdenes",
                               font=ctk.CTkFont(size=24, weight="bold"), text_color=COLOR_TEXT)
    title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    # Barra de Herramientas (Búsqueda y Filtros) 
    toolbar_frame = ctk.CTkFrame(historial_frame, fg_color="transparent")
    toolbar_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
    toolbar_frame.grid_columnconfigure(0, weight=1) # Columna de búsqueda
    
    # Campo de Búsqueda
    search_entry = ctk.CTkEntry(toolbar_frame, placeholder_text="Buscar órdenes...",
                                fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY,
                                text_color=COLOR_TEXT, width=300)
    search_entry.grid(row=0, column=0, padx=(0, 10), sticky="w")
    
    # Botón "Mostrar todas las órdenes"
    show_all_button = ctk.CTkButton(toolbar_frame, text="Mostrar todas",
                                    fg_color=COLOR_SECONDARY, hover_color=COLOR_PRIMARY,
                                    text_color=COLOR_TEXT)
    show_all_button.grid(row=0, column=1, padx=5, sticky="e")

    # Botón "Ordenar por"
    sort_by_button = ctk.CTkButton(toolbar_frame, text="Ordenar por fecha 📅",
                                   fg_color=COLOR_SECONDARY, hover_color=COLOR_PRIMARY,
                                   text_color=COLOR_TEXT)
    sort_by_button.grid(row=0, column=2, padx=(5, 0), sticky="e")
    
    # Esto empuja los botones de filtro/ordenamiento a la derecha
    toolbar_frame.grid_columnconfigure(1, weight=0)
    toolbar_frame.grid_columnconfigure(2, weight=0)

    #  3. Información de la Tabla 
    info_label = ctk.CTkLabel(historial_frame, text="Mostrando: 1 de 1 items",
                              font=ctk.CTkFont(size=14), text_color=COLOR_TEXT)
    info_label.grid(row=2, column=0, padx=20, pady=(10, 5), sticky="w")
    
    #  4. Contenedor de la Tabla (Treeview) 
    table_container = ctk.CTkFrame(historial_frame, fg_color=COLOR_BG_CARD)
    table_container.grid(row=3, column=0, padx=20, pady=(5, 20), sticky="nsew")
    table_container.grid_rowconfigure(0, weight=1)
    table_container.grid_columnconfigure(0, weight=1)
    
    # Creamos un Treeview de Tkinter para la tabla ya que CustomTkinter no tiene una tabla nativa.
    # Necesitamos aplicar estilos de ttk para que se vea bien en CTk.
    
    style = ttk.Style()
    
    # Estilo de la tabla (Treeview) para que se ajuste al tema oscuro
    style.theme_use("default") # Inicia con el tema base
    style.configure("Custom.Treeview", 
                    background=COLOR_BG_CARD, 
                    foreground=COLOR_TEXT,
                    rowheight=25, 
                    fieldbackground=COLOR_BG_CARD,
                    bordercolor=COLOR_BG_CARD,
                    borderwidth=0)
    
    # Estilo de los encabezados de la tabla
    style.configure("Custom.Treeview.Heading", 
                    background=COLOR_SECONDARY, 
                    foreground=COLOR_TEXT, 
                    font=('Arial', 10, 'bold'),
                    bordercolor=COLOR_BG_CARD)
    
    # Cuando seleccionamos una fila
    style.map('Custom.Treeview',
              background=[('selected', COLOR_SECONDARY)],
              foreground=[('selected', COLOR_TEXT)])

    
    columns = ("id", "date", "customer", "payment", "delivery", "total")
    tree = ttk.Treeview(table_container, columns=columns, show="headings", style="Custom.Treeview")

    # Definición de Encabezados (ajustados a una cafetería)
    tree.heading("id", text="ID Orden")
    tree.heading("date", text="Fecha")
    tree.heading("customer", text="Cliente")
    tree.heading("payment", text="Pago")
    tree.heading("delivery", text="Entrega")
    tree.heading("total", text="Total")

    # Definición del ancho de las columnas
    tree.column("id", width=80, anchor='center')
    tree.column("date", width=120, anchor='center')
    tree.column("customer", width=150, anchor='w')
    tree.column("payment", width=100, anchor='center')
    tree.column("delivery", width=100, anchor='center')
    tree.column("total", width=100, anchor='e') # e = east (derecha para números)

    # # Datos de ejemplo (simulando los datos de la imagen adjunta)
    # data = [
    #     ("1001", "27 Oct 2023", "John Smith", "Pagado", "Entregado", "$0.50"),
    #     ("1002", "27 Oct 2023", "Jane Doe", "Pendiente", "Recoger", "$12.99"),
    #     ("1003", "28 Oct 2023", "Peter Parker", "Pagado", "A Domicilio", "$8.75"),
    # ]

    # Obtenemos los datos reales del controlador
    try:
        data = obtener_historial_ordenes()  # Suponiendo que devuelve una lista de tuplas
    except Exception as e:
        data = []
        info_label.configure(text=f"Error al cargar datos: {e}")   

    for item in data:
        # Insertar datos en la tabla. Agregamos tags para colorear estados (como en la imagen)
        tags = ()
        if "Pagado" in item:
            tags = ('paid',)
        elif "Pendiente" in item:
            tags = ('pending',)
            
        tree.insert('', 'end', values=item, tags=tags)
    info_label.configure(text=f"Mostrando: {len(data)} items")
    # Colorear las celdas de "Pago" y "Entrega" (requiere un poco más de trabajo con ttk)
    # Customizamos el estilo de la fila para los tags
    # Nota: Colorear celdas individuales es complejo en Treeview.
    # En este ejemplo, solo colorearemos el fondo de la fila por simplicidad,
    # aunque en el diseño original solo se colorea el campo de estado.
    # Para simular el diseño original, podrías usar un Treeview y luego etiquetas
    # o frames encima de él, o usar un widget de tabla más avanzado.
    
    # Por ahora, solo coloreamos el texto para simular estados de "Pagado" y "Entregado"
    # El estilo de la tabla ya se configuró.

    tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    # Scrollbar vertical (opcional, pero útil si hay muchas órdenes)
    vsb = ctk.CTkScrollbar(table_container, orientation="vertical", command=tree.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    tree.configure(yscrollcommand=vsb.set)


    return historial_frame

