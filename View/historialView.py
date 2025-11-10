import customtkinter as ctk
from tkinter import ttk  
from Controller.Venta_Controller import VentaController

# ------ REGISTRO/HISTORIAL DE VENTAS ------
def crear_vista_historial(parent_frame, paleta):
    
    #llamando el controlador
    controller = VentaController()
    global historialEstatico
    #cargar numero de items desplegados
    no_items = 0

    def CargarHistorial(historialActualizado = None):
        global historialEstatico
        #cargar en el estado global
        if historialActualizado is None:
            historialActualizado = controller.HistorialVenta()
        historialEstatico = historialActualizado
        
        for item in tree.get_children():
            tree.delete(item)
        for NoVenta, Fecha, NombreEmpl, NombreCl, NombrePro, PrecioUni, CantidadOrd, TotalVenta in historialActualizado:
            tree.insert('', 'end', values=(NoVenta, Fecha, NombreEmpl, NombreCl, NombrePro, PrecioUni, CantidadOrd, TotalVenta))
        info_label.configure(text=f"Mostrando: {len(historialActualizado)} items")
        
    def FiltrarHistorial(variable):
        if variable == "Por fecha(mas reciente)":
            CargarHistorial(controller.Historial_Fecha_DESC())
        if variable == "Por fecha(menos reciente)":
            CargarHistorial(controller.Historial_Fecha_ASC())
        if variable == "Por Total(mayor)":
            CargarHistorial(controller.Historial_Total_DESC())
        if variable == "Por Total(menor)":
            CargarHistorial(controller.Historial_Total_ASC())
            
    def BuscarDatos(event):
        query = EtyBuscar.get().lower()
        for item in tree.get_children():
            tree.delete(item)
        for row in historialEstatico:
            # comparamos todos los campos como cadena en minúsculas
            if (query in str(row[0]).lower() or
                query in str(row[1]).lower() or
                query in str(row[2]).lower() or
                query in str(row[3]).lower() or
                query in str(row[4]).lower() or
                query in str(row[5]).lower() or
                query in str(row[6]).lower() or
                query in str(row[7]).lower()):
                # insertar sólo una vez
                tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    # Definición de Colores 
    COLOR_PRIMARY = paleta['principal']
    COLOR_SECONDARY = paleta['secundario']
    COLOR_TEXT = paleta['texto']
    COLOR_BG_CARD = paleta['tarjeta']

    #  Frame Principal de la Vista 
    HistorialFrame = ctk.CTkFrame(parent_frame, fg_color=COLOR_PRIMARY)
    HistorialFrame.grid_columnconfigure(0, weight=1)
    HistorialFrame.grid_rowconfigure(3, weight=1) # Fila para la tabla

    # Título de la Vista 
    lblTitulo = ctk.CTkLabel(HistorialFrame, text="Órdenes",
                               font=ctk.CTkFont(size=24, weight="bold"), text_color=COLOR_TEXT)
    lblTitulo.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

    # Barra de Herramientas (Búsqueda y Filtros) 
    OpcionesFrame = ctk.CTkFrame(HistorialFrame, fg_color="transparent")
    OpcionesFrame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
    OpcionesFrame.grid_columnconfigure(0, weight=1) # Columna de búsqueda
    
    # Campo de Búsqueda
    EtyBuscar = ctk.CTkEntry(OpcionesFrame, placeholder_text="Buscar órdenes...",
                                fg_color=COLOR_BG_CARD, border_color=COLOR_SECONDARY,
                                text_color=COLOR_TEXT, width=300)
    EtyBuscar.grid(row=0, column=0, padx=(0, 10), sticky="w")
    
    #Bind para la funcion buscar datos
    EtyBuscar.bind("<KeyRelease>", BuscarDatos)
    
    # Botón "Mostrar todas las órdenes"
    BtnMostrarTodo = ctk.CTkButton(OpcionesFrame, text="Mostrar todas",
                                    fg_color=COLOR_SECONDARY, hover_color=COLOR_PRIMARY,
                                    text_color=COLOR_TEXT,
                                    command=CargarHistorial)
    BtnMostrarTodo.grid(row=0, column=1, padx=5, sticky="e")

    # Botón "Ordenar por"
    Cmbx_values = ("Por fecha(mas reciente)","Por fecha(menos reciente)",
                   "Por Total(mayor)","Por Total(menor)")
    Cmbx_ordenar_por = ctk.CTkComboBox(OpcionesFrame, fg_color=COLOR_SECONDARY, values=Cmbx_values, 
                                       text_color=COLOR_TEXT, state="readonly", command=FiltrarHistorial)
    Cmbx_ordenar_por.grid(row=0, column=2, padx=(5, 0))
    Cmbx_ordenar_por.set("Por fecha(mas reciente)")
    
    # Esto empuja los botones de filtro/ordenamiento a la derecha
    OpcionesFrame.grid_columnconfigure(1, weight=0)
    OpcionesFrame.grid_columnconfigure(2, weight=0)

    #  3. Información de la Tabla 
    info_label = ctk.CTkLabel(HistorialFrame, text=f"Mostrando: {no_items} de 1 items",
                              font=ctk.CTkFont(size=14), text_color=COLOR_TEXT)
    info_label.grid(row=2, column=0, padx=20, pady=(10, 5), sticky="w")
    
    #  4. Contenedor de la Tabla (Treeview) 
    table_container = ctk.CTkFrame(HistorialFrame, fg_color=COLOR_BG_CARD)
    table_container.grid(row=3, column=0, padx=20, pady=(5, 20), sticky="nsew")
    table_container.grid_rowconfigure(0, weight=1)
    table_container.grid_columnconfigure(0, weight=1)
    
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

    
    columns = ("Noventa", "Fecha", "Empleado", "Cliente", "Producto", "PrecioUni", "Cantidad", "TotalCompra")
    tree = ttk.Treeview(table_container, columns=columns, show="headings", style="Custom.Treeview")

    # Definición de Encabezados (ajustados a una cafetería)
    tree.heading("Noventa", text="No. Venta")
    tree.heading("Fecha", text="Fecha")
    tree.heading("Empleado", text="Empleado")
    tree.heading("Cliente", text="Cliente")
    tree.heading("Producto", text="Producto")
    tree.heading("PrecioUni", text="Precio unitario")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("TotalCompra", text="Total de Compra")

    # Definición del ancho de las columnas
    tree.column("Noventa", width=30, anchor='center')
    tree.column("Fecha", width=100, anchor='center')
    tree.column("Empleado", width=100, anchor='center')
    tree.column("Cliente", width=150, anchor='w')
    tree.column("Producto", width=150, anchor='center')
    tree.column("PrecioUni", width=100, anchor='center')
    tree.column("Cantidad", width=20, anchor='center') # e = east (derecha para números)
    tree.column("TotalCompra", width=30, anchor='w')
    
    #CargarDatos
    CargarHistorial()

    # El estilo de la tabla ya se configuró.
    tree.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    # # Scrollbar vertical (opcional, pero útil si hay muchas órdenes)
    vsb = ctk.CTkScrollbar(table_container, orientation="vertical", command=tree.yview)
    vsb.grid(row=0, column=1, sticky='ns')
    tree.configure(yscrollcommand=vsb.set)
    # vsbx = ctk.CTkScrollbar(table_container, orientation="horizontal", command=tree.xview)
    # vsbx.grid(row=0, column=1, sticky='ew')
    # tree.configure(yscrollcommand=vsbx.set)

    return HistorialFrame

