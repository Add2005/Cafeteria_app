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
    marco_productos = ctk.CTkScrollableFrame(vista_menu, label_text="Escoge tu Plato", fg_color=colores.get('principal'))
    marco_productos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Derecha: resumen de orden (placeholder)
    marco_orden = ctk.CTkFrame(vista_menu, fg_color=colores.get('tarjeta'))
    marco_orden.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    ctk.CTkLabel(marco_orden, text="Confirmacion de Orden", text_color=colores.get('texto'), font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="nw", padx=12, pady=12)

    return vista_menu
