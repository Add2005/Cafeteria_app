import customtkinter as ctk
from Controller.producto_Controller import ProductoController
from PIL import Image

# trayendo los datos a el form con el controller
control = ProductoController()
# declarando listas para las categorias
Cafes = list()
BebidasFrias = list()
Postres = list()
for ca in control.ListarCafes():
    Cafes.append(ca)
for bebidas in control.ListarBebidasFrias():
    BebidasFrias.append(bebidas)
for pst in control.ListarPostres():
    Postres.append(pst)


def crear_vista_menu(parent, colores):
    """Crea y devuelve el frame de la vista 'menu'.
    parent: widget contenedor donde se colocara el frame
    colores: dict con claves 'principal', 'secundario', 'texto', 'tarjeta'
    """

    vista_menu = ctk.CTkFrame(parent, fg_color=colores.get('principal'))
    vista_menu.grid(row=0, column=0, sticky="nsew")

    vista_menu.grid_columnconfigure(0, weight=2)
    vista_menu.grid_columnconfigure(1, weight=1)
    vista_menu.grid_rowconfigure(0, weight=1)

    # Izquierda: lista de productos
    marco_productos = ctk.CTkScrollableFrame(vista_menu,
                                            label_text="Escoge tu Plato",
                                            fg_color=colores.get('principal'))
    marco_productos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # BOTONES DE CATEGORIAS debajo del header de productos
    categorias_frame = ctk.CTkFrame(marco_productos, fg_color=colores.get('principal'))
    categorias_frame.pack(pady=(10, 5))
    categorias = ["Cafes👅", "Postres🍑", "Bebidas Frías🥶"]
    for cat in categorias:
        boton = ctk.CTkButton(
            categorias_frame,
            text=cat,
            width=120,
            height=40,
            fg_color=colores.get('secundario'),
            text_color=colores.get('texto'),
            font=ctk.CTkFont(size=14, weight="bold"),
            hover_color=colores.get('principal'),
            command=lambda c=cat: mostrar_productos(c)
        )
        boton.pack(side="left", padx=5)

    # Derecha: resumen de orden (placeholder)
    marco_orden = ctk.CTkFrame(vista_menu, fg_color=colores.get('tarjeta'))
    marco_orden.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    marco_orden.grid_rowconfigure(1, weight=1)
    marco_orden.grid_columnconfigure(0, weight=1)

    # Panel derecho: encabezado
    header_frame = ctk.CTkFrame(marco_orden, fg_color="transparent")
    header_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=15)
    lbl_title = ctk.CTkLabel(
        header_frame,
        text="Confirmación de Orden",
        text_color=colores.get('texto'),
        font=ctk.CTkFont(size=18, weight="bold")
    )
    lbl_title.pack(anchor="w")

    # Area para mostrar items (scrollable)
    items_scroll = ctk.CTkScrollableFrame(
        marco_orden,
        fg_color="transparent",
        scrollbar_button_color=colores.get('secundario'),
        height=250
    )
    items_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0,10))

    # Estado de la orden
    order_items = {}  # {nombre: {'precio': float, 'cantidad': int}}

    def calculate_totals():
        subtotal = sum(v['precio'] * v['cantidad'] for v in order_items.values())
        total = subtotal
        return subtotal, total

    def refresh_order_view():
        # limpiar el scrollable
        for w in items_scroll.winfo_children():
            w.destroy()

        # si no hay items mostramos mensaje
        if not order_items:
            ctk.CTkLabel(
                items_scroll,
                text="Tu orden está vacía\n\n🛒",
                text_color=colores.get('texto'),
                font=ctk.CTkFont(size=14)
            ).pack(expand=True, pady=50)
        else:
            # crear fila por cada item
            for name, data in order_items.items():
                row = ctk.CTkFrame(items_scroll, fg_color=colores.get('tarjeta'))
                row.pack(fill="x", pady=4, padx=4)

                ctk.CTkLabel(row, text=f"{name} x{data['cantidad']}", text_color=colores.get('texto')).pack(side="left", padx=8)

                controls = ctk.CTkFrame(row, fg_color="transparent")
                controls.pack(side="right", padx=8)

                def make_inc(n):
                    return lambda: (order_items.__setitem__(n, {'precio': order_items[n]['precio'], 'cantidad': order_items[n]['cantidad'] + 1}), refresh_order_view())

                def make_dec(n):
                    def _dec():
                        order_items[n]['cantidad'] -= 1
                        if order_items[n]['cantidad'] <= 0:
                            del order_items[n]
                        refresh_order_view()
                    return _dec

                ctk.CTkButton(controls, text="+", width=30, command=make_inc(name)).pack(side="right", padx=4)
                ctk.CTkButton(controls, text="-", width=30, command=make_dec(name)).pack(side="right")

        subtotal, total = calculate_totals()
        subtotal_label.configure(text=f"Subtotal: ${subtotal:.2f}")
        total_label.configure(text=f"Total: ${total:.2f}")

    # Totales
    totales_frame = ctk.CTkFrame(marco_orden, fg_color="transparent")
    totales_frame.grid(row=2, column=0, sticky="ew", padx=15, pady=(0,10))

    subtotal_label = ctk.CTkLabel(
        totales_frame,
        text="Subtotal: $0.00",
        text_color=colores.get('texto'),
        font=ctk.CTkFont(size=14, weight="bold")
    )
    subtotal_label.pack(anchor="e", pady=2)

    total_label = ctk.CTkLabel(
        totales_frame,
        text="Total: $0.00",
        text_color=colores.get('texto'),
        font=ctk.CTkFont(size=16, weight="bold")
    )
    total_label.pack(anchor="e", pady=2)

    # Botones de accion (mantener comportamiento top-level para confirmar pago)
    botones_frame = ctk.CTkFrame(marco_orden, fg_color="transparent")
    botones_frame.grid(row=3, column=0, sticky="ew", padx=15, pady=(0,15))

    # Helper para añadir items desde las tarjetas
    def make_add(nombre, precio):
        def _add():
            if nombre in order_items:
                order_items[nombre]['cantidad'] += 1
            else:
                order_items[nombre] = {'precio': precio, 'cantidad': 1}
            refresh_order_view()
        return _add

    # Botón descartar (limpia orden)
    clean_btn = ctk.CTkButton(
        botones_frame,
        text="Descartar Orden",
        fg_color= colores.get('secundario'),
        hover_color=colores.get('principal'),
        text_color=colores.get('texto'),
        font=ctk.CTkFont(size=14, weight="bold"),
        command=lambda: (order_items.clear(), refresh_order_view()),
        height=40
    )
    clean_btn.pack(fill="x", pady=(0,8))

    # Funcionalidad top-level para confirmar pago (mantenida como en el pull)
    def WindowPago():
        # Crear la window emergent
        window_pago = ctk.CTkToplevel(vista_menu)
        window_pago.title("Confirmar Pago")
        window_pago.geometry("600x800")
        window_pago.lift()
        window_pago.focus_force()
        window_pago.grab_set()
        window_pago.resizable(False, True)

        # Encabezado
        headerPagos = ctk.CTkLabel(
            window_pago,
            text="Payment Confirmacion\nRevieu your order and select payment method",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=colores.get('texto'),
            justify="center"
        )
        headerPagos.pack(pady=(20, 10))

        # Marco de items
        marco_items = ctk.CTkScrollableFrame(
            window_pago,
            fg_color=colores.get('tarjeta'),
            label_text="Ordered Items"
        )
        marco_items.pack(fill="both", expand=True, padx=20, pady=10)

        # Poblamos los items en el toplevel
        if not order_items:
            ctk.CTkLabel(marco_items, text="No hay items en la orden.", text_color=colores.get('texto')).pack(pady=20)
        else:
            for name, data in order_items.items():
                ctk.CTkLabel(marco_items, text=f"{name} x{data['cantidad']}  -  ${data['precio']*data['cantidad']:.2f}", text_color=colores.get('texto')).pack(anchor='w', padx=10, pady=4)

        # payment method
        paymentFrame = ctk.CTkFrame(window_pago, fg_color=colores.get('tarjeta'), width= 100, height=100)
        paymentFrame.pack(padx=20, pady=5)

        metodo_pago = ctk.StringVar(value="Cash")
        ctk.CTkRadioButton(paymentFrame, text="Cash 🏳️‍⚧️ ", variable=metodo_pago, value="Cash").pack(anchor="w", padx=10, pady=5)
        ctk.CTkRadioButton(paymentFrame, text="Card 💳", variable=metodo_pago, value="Card").pack(anchor="w", padx=10, pady=5)

        # Totales en toplevel
        total_frame = ctk.CTkFrame(window_pago, fg_color=colores.get('tarjeta'), width= 120, height=100)
        total_frame.pack(padx=20, pady=(20, 20))

        ctk.CTkLabel(total_frame, text="Total a pagar:", font=ctk.CTkFont(size=14, weight="bold")).grid(row=0, column=0, sticky="w", pady=5)
        lbl_total = ctk.CTkLabel(total_frame, text=f"${calculate_totals()[1]:.2f}", font=ctk.CTkFont(size=14))
        lbl_total.grid(row=0, column=1, sticky="e", pady=5)

        ctk.CTkLabel(total_frame, text="Total recibido:", font=ctk.CTkFont(size=14, weight="bold")).grid(row=1, column=0, sticky="w", pady=5)
        entry_recibido = ctk.CTkEntry(total_frame, placeholder_text="Recibido", width=100)
        entry_recibido.grid(row=1, column=1, sticky="e", pady=5)

        ctk.CTkLabel(total_frame, text="Vuelto a dar:", font=ctk.CTkFont(size=14, weight="bold")).grid(row=2, column=0, sticky="w", pady=5)
        lbl_vuelto = ctk.CTkLabel(total_frame, text="$0.00", font=ctk.CTkFont(size=14))
        lbl_vuelto.grid(row=2, column=1, sticky="e", pady=5)

        lbl_mainpago = ctk.CTkLabel(
            window_pago,
            text="¿Deseas confirmar el pago?",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        lbl_mainpago.pack(pady=20)

        botones_pagos = ctk.CTkFrame(window_pago)
        botones_pagos.pack(pady=10)

        def confirmar_pago():
            # Aquí integrar con Controller/Model para guardar la orden
            print("Pago confirmado 🧼")
            order_items.clear()
            refresh_order_view()
            window_pago.destroy()

        btn_pagoConfirmar = ctk.CTkButton(
            botones_pagos,
            text="Sí, confirmar",
            fg_color=colores.get('secundario'),
            hover_color=colores.get('principal'),
            text_color=colores.get('texto'),
            command=confirmar_pago
        )
        btn_pagoConfirmar.pack(side="left", padx=10)

        btn_pagoCancelar = ctk.CTkButton(
            botones_pagos,
            text="Cancelar",
            fg_color="gray",
            hover_color="white",
            text_color="white",
            command=window_pago.destroy
        )
        btn_pagoCancelar.pack(side="left", padx=10)

    # Botón pagar (abre el top-level)
    pay_btn = ctk.CTkButton(
        botones_frame,
        text="Confirmar Pago",
        fg_color=colores.get('secundario'),
        hover_color=colores.get('principal'),
        text_color=colores.get('texto'),
        height=40,
        font=ctk.CTkFont(size=14, weight="bold"),
        command=WindowPago
    )
    pay_btn.pack(fill="x")

    # Mostrar productos por defecto
    def cambiar_categoria(cat):
        mostrar_productos(cat)

    productos = {
        "Cafes👅": Cafes,
        "Postres🍑": Postres,
        "Bebidas Frías🥶": BebidasFrias
    }

    # crear contenedor de productos y mostrar por defecto Cafes
    productos_frame = ctk.CTkFrame(marco_productos, fg_color=colores.get('principal'))
    productos_frame.pack(fill="both", expand=True)

    def mostrar_productos(categoria):
        # Limpiar productos anteriores
        for widget in productos_frame.winfo_children():
            widget.destroy()

        # Crear grid para organizar productos
        productos_grid = ctk.CTkFrame(productos_frame, fg_color=colores.get('principal'))
        productos_grid.pack(fill="both", expand=True, padx=5)

        # Obtener lista de productos
        items = productos.get(categoria, [])

        # Si no hay items en la categoría, mostrar mensaje
        if not items:
            empty = ctk.CTkLabel(productos_frame, text="No hay productos en esta categoría.", text_color=colores.get('texto'))
            empty.pack(pady=20)
            return

        # Crear tarjeta por cada producto
        for idxy, (nombre, descripcion, precio) in enumerate(items):
            tarjeta = ctk.CTkFrame(
                productos_grid,
                fg_color=colores.get('tarjeta'),
                corner_radius=20
            )
            tarjeta.grid(row=idxy//2, column=idxy%2, padx=10, pady=10, sticky="nsew")
            tarjeta.grid_columnconfigure(0, weight=1)

            img_frame = ctk.CTkFrame(
                tarjeta,
                fg_color=colores.get('principal'),
                height=120,
                corner_radius=10
            )
            img_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
            img_frame.grid_propagate(True)

            try:
                ImgProducto = "imgs/reportes.png"
                prod_img = Image.open(ImgProducto).resize((30, 30))
                ImgProducto = ctk.CTkImage(light_image=prod_img, dark_image=prod_img, size=(80, 80))
            except Exception:
                ImgProducto = None

            ctk.CTkLabel(
                img_frame,
                text="",
                image=ImgProducto,
                font=ctk.CTkFont(size=40)
            ).place(relx=0.5, rely=0.5, anchor="center")

            info_frame = ctk.CTkFrame(tarjeta, fg_color="transparent")
            info_frame.grid(row=1, column=0, padx=10, pady=(0,5), sticky="ew")

            ctk.CTkLabel(
                info_frame,
                text=nombre,
                font=ctk.CTkFont(size=15, weight="bold"),
                text_color=colores.get('texto'),
                anchor="w"
            ).pack(anchor="w", pady=(0,2))

            ctk.CTkLabel(
                info_frame,
                text=descripcion,
                text_color=colores.get('texto'),
                font=ctk.CTkFont(size=11),
                anchor="w",
                wraplength=200
            ).pack(anchor="w", pady=(0,5))

            bottom_frame = ctk.CTkFrame(tarjeta, fg_color="transparent")
            bottom_frame.grid(row=2, column=0, padx=10, pady=(0,10), sticky="ew")
            bottom_frame.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(
                bottom_frame,
                text=f"${precio:.2f}",
                text_color=colores.get('texto'),
                font=ctk.CTkFont(size=16, weight="bold")
            ).grid(row=0, column=0, sticky="w")

            # Botón añadir: ahora llama al helper make_add para añadir al order_items
            add_btn = ctk.CTkButton(
                bottom_frame,
                text="Añadir",
                width=80,
                height=32,
                fg_color=colores.get('secundario'),
                text_color=colores.get('texto'),
                hover_color="#d364ff",
                font=ctk.CTkFont(size=12, weight="bold"),
                corner_radius=8,
                command=make_add(nombre, precio)
            )
            add_btn.grid(row=0, column=1, sticky="e")

        productos_grid.grid_columnconfigure(0, weight=1, uniform="col")
        productos_grid.grid_columnconfigure(1, weight=1, uniform="col")

    mostrar_productos("Cafes👅")

    return vista_menu
        #fun confirmar
