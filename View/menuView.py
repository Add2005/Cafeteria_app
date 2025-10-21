import customtkinter as ctk

def crear_vista_menu(parent, colores):
    """
    crea y deveulve el frame de la vista 'menu'.
    parent: widget contenedor donde se colocara el frame
    colores: dict con claves 'principal', 'secundario', 'texto', 'tarjeta'
    """
    vista_menu = ctk.CTkFrame(parent, fg_color=colores.get('principal'))
    vista_menu.grid(row=0, column=0, sticky="nsew")

    vista_menu.grid_columnconfigure(0, weight=2)
    vista_menu.grid_columnconfigure(1, weight=1)
    vista_menu.grid_rowconfigure(0, weight=1)

    # Izquierda: lista de productos (placeholder)
    marco_productos = ctk.CTkScrollableFrame(vista_menu,
                                            label_text="Escoge tu Plato",
                                            fg_color=colores.get('principal')    ) 
    marco_productos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Derecha: resumen de orden (placeholder)
    marco_orden = ctk.CTkFrame(vista_menu, fg_color=colores.get('tarjeta'))
    marco_orden.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    ctk.CTkLabel(marco_orden, text="Confirmacion de Orden", text_color=colores.get('texto'), font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="nw", padx=12, pady=12)



# --- BOTONES DE CATEGORIAS ---
#--------------------------------------------
    categorias_frame = ctk.CTkFrame(marco_productos, fg_color=colores.get('principal')) # ctk.CTkFrame es el contenedor 
    categorias_frame.pack( pady=(10, 5))
#lista de cat
    categorias = ["Cafes👅", "Postres🍑", "Bebidas Frías🥶"]
    botones_categoria = {} #almacenar los botones para cambiar su estado
#definir la función para cambiar de categoría
    def cambiar_categoria(cat):
        mostrar_productos(cat)

#for para crear los botones de categoría y no repetir código 
# boton_cafes = ctk.CTkButton(categoras_frame,
#     text="Cafes👅",
#     width=80,
#     height=25,
#     fg_color=colores.get('secundario'),
#     text_color=colores.get('texto'),
#     command=lambda: cambiar_categoria("Cafes👅"))
# boton_cafes.pack(side="left", padx=5)
# botones_categoria["Cafes👅"] = boton_cafes

    for cat in categorias:
            boton = ctk.CTkButton(
                categorias_frame,
                text=cat,
                width=120, 
                height=40,
                fg_color=colores.get('secundario'), #if cat == "Cafes👅" else colores.get('tarjeta'), test🧼
                text_color=colores.get('texto'),
                font=ctk.CTkFont(size=14, weight="bold"),
                hover_color=colores.get('principal'),
                command=lambda c=cat: cambiar_categoria(c)
            )
            boton.pack(side="left", padx=5)
            botones_categoria[cat] = boton
            



    # --- MARCO PRODUCTOS ---============================================
    productos_frame = ctk.CTkFrame(marco_productos, fg_color=colores.get('principal'))
    productos_frame.pack(fill="both", expand=True)

    # --- DATOS DE LOS PRODUCTOS (INCODE PARA EJEMPLO)--- = productos = {categoria[(titulo, desc, precio)]}
    productos = {
        "Cafes👅": [
            ("Latte Caramelo ", "El más vendido, suave y dulce.", 4.50),
            ("Cappuccino Clásico", "Espresso, leche vaporizada y espuma.", 3.80),
            ("Moka Oscura", "Chocolate intenso y doble shot de espresso.", 5.00),
            ("Affogato", "Helado de vainilla con shot de espresso.", 5.50)
        ],
        "Postres🍑": [
            ("⁉Tarta de Manzana", "Porción de tarta casera.", 4.00),
            ("Croissant", "Recién horneado con mantequilla.", 2.50)
        ],
        "Bebidas Frías🥶": [
            ("Cold Brew", "Café infusionado en frío por 12 horas.", 3.50),
            ("Frappe de Vainilla", "Cremoso y refrescante.", 4.00)
        ]
    }


#mostrar productos con png
    def mostrar_productos(categoria): #muestra los productos de la categoria seleccionada (categoria)
        # Limpiar productos anteriores
        for widget in productos_frame.winfo_children():
            widget.destroy()

        # Crear grid para organizar productos
        productos_grid = ctk.CTkFrame(productos_frame, fg_color=colores.get('principal'))
        productos_grid.pack(fill="both", expand=True, padx=5)

        # Obtener lista de productos
        items = productos.get(categoria, [])
        
#Crear tarjeta por cada producto
        for idxy, (nombre, descripcion, precio) in enumerate(items): 
            # Tarjeta del producto
            tarjeta = ctk.CTkFrame(
                productos_grid, 
                fg_color=colores.get('tarjeta'), 
                corner_radius=20 #
            )
            tarjeta.grid(row=idxy//2, column=idxy%2, padx=10, pady=10, sticky="nsew")
            tarjeta.grid_columnconfigure(0, weight=1)

# Imagen del producto (por ahora un emoji grande)
            img_frame = ctk.CTkFrame(
                tarjeta, 
                fg_color=colores.get('principal'), 
                height=120, 
                corner_radius=10
            )
            img_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
            img_frame.grid_propagate(True) # evitar que el frame cambie de tamaño
            
            ctk.CTkLabel(
                img_frame, 
                text="🍽️", 
                font=ctk.CTkFont(size=40)
            ).place(relx=0.5, rely=0.5, anchor="center")

            # Información del producto
            info_frame = ctk.CTkFrame(tarjeta, fg_color="transparent")
            info_frame.grid(row=1, column=0, padx=10, pady=(0,5), sticky="ew")

# Nombre
            ctk.CTkLabel(
                info_frame, 
                text=nombre, 
                font=ctk.CTkFont(size=15, weight="bold"),
                text_color=colores.get('texto'),
                anchor="w"
            ).pack(anchor="w", pady=(0,2))

           
            ctk.CTkLabel( # Descripción
                info_frame, 
                text=descripcion, 
                text_color=colores.get('texto'),
                font=ctk.CTkFont(size=11),
                anchor="w",
                wraplength=200 #ajustar texto a 200px de ancho 
            ).pack(anchor="w", pady=(0,5))

            # Precio y botón
            bottom_frame = ctk.CTkFrame(tarjeta, fg_color="transparent")
            bottom_frame.grid(row=2, column=0, padx=10, pady=(0,10), sticky="ew")
            bottom_frame.grid_columnconfigure(0, weight=1)

            # Precio
            ctk.CTkLabel(
                bottom_frame, 
                text=f"${precio:.2f}", 
                text_color=colores.get('texto'),
                font=ctk.CTkFont(size=16, weight="bold")
            ).grid(row=0, column=0, sticky="w")

            # Botón añadir (por ahora solo visual)
            ctk.CTkButton(
                bottom_frame, 
                text="Añadir", 
                width=80, 
                height=32,
                fg_color=colores.get('secundario'),
                text_color=colores.get('texto'),
                hover_color="#d364ff",
                font=ctk.CTkFont(size=12, weight="bold"),
                corner_radius=8
            ).grid(row=0, column=1, sticky="e")

        # Hacer que las columnas tengan el mismo tamaño
        productos_grid.grid_columnconfigure(0, weight=1, uniform="col") 
        productos_grid.grid_columnconfigure(1, weight=1, uniform="col")
#-------------end


# SECCIÓN: PANEL DERECHO - CONFIRMACIÓN DE ORDEN
    marco_orden = ctk.CTkFrame(
        vista_menu, 
        fg_color=colores.get('tarjeta'), 
        corner_radius=15
    )
    marco_orden.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    marco_orden.grid_rowconfigure(1, weight=1)
    marco_orden.grid_columnconfigure(0, weight=1)

# Título del panel
    header_frame = ctk.CTkFrame(marco_orden, fg_color="transparent")
    header_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=15)
    
    ctk.CTkLabel(
        header_frame, 
        text="Confirmación de Orden", 
        text_color=colores.get('texto'), 
        font=ctk.CTkFont(size=18, weight="bold")
    ).pack(anchor="w")

    # Área para mostrar items (vacía)
    items_scroll = ctk.CTkScrollableFrame(
        marco_orden, 
        fg_color="transparent",
        scrollbar_button_color=colores.get('secundario')
    )
    items_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0,10))

    # Mensaje de carrito vacío
    ctk.CTkLabel(
        items_scroll,
        text="Tu orden está vacía\n\n🛒",
        text_color=colores.get('texto'),
        font=ctk.CTkFont(size=14)
    ).pack(expand=True, pady=50)

    # Totales
    totales_frame = ctk.CTkFrame(marco_orden, fg_color="transparent")
    totales_frame.grid(row=2, column=0, sticky="ew", padx=15, pady=(0,10))

    ctk.CTkLabel(
        totales_frame,
        text="Subtotal: $0.00", #agregar command para actualizar
        text_color=colores.get('texto'),
        font=ctk.CTkFont(size=14, weight="bold")
    ).pack(anchor="e", pady=2)

    ctk.CTkLabel(
        totales_frame,
        text="Total: $0.00", #agregar command para actualizar
        text_color=colores.get('texto'),
        font=ctk.CTkFont(size=16, weight="bold")
    ).pack(anchor="e", pady=2)











#----------------- end

    #botones de acción lado derecho 
    botones_frame = ctk.CTkFrame(marco_orden, fg_color="transparent")
    botones_frame.grid(row=3, column=0, sticky="ew", padx=15, pady=(0,15))
    
    # Botón limpiar
    ctk.CTkButton(
        botones_frame,
        text="Descartar Orden",
        fg_color= colores.get('secundario'),
        hover_color=colores.get('principal'),
        text_color=colores.get('texto'),
        font=ctk.CTkFont(size=14, weight="bold"),
        command=lambda: print("Orden descartada"),
        height=40
    ).pack(fill="x", pady=(0,8))

    # Botón pagar
    ctk.CTkButton(
        botones_frame,
        text="Confirmar Pago",
        fg_color=colores.get('secundario'),
        hover_color=colores.get('principal'),
        text_color=colores.get('texto'),
        height=40,
        font=ctk.CTkFont(size=14, weight="bold"),
        command=lambda: print("Pago confirmado")
    ).pack(fill="x")
#----------------- end


    return vista_menu
