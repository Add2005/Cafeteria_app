#utils xd
from datetime import datetime
import time 
import customtkinter as ctk
from tkinter import messagebox
#Entidades
from Entities.usuario import usuario
from Entities.detalle_venta import detalle_venta
from Entities.venta import Venta
#Controladores
from Controller.producto_Controller import ProductoController
from Services.Venta_Service import VentaService


# Funcionalidad top-level para confirmar pago (mantenida como en el pull)
def WindowPago(vista_menu, colores, calculate_total, order_items):
    
    #Cargar VentaController
    controlProducto = ProductoController()
    serviceVenta = VentaService()
    
    # Crear la window emergent
    window_pago = ctk.CTkToplevel(vista_menu)
    window_pago.title("Confirmar Pago")
    window_pago.geometry("500x700")
    window_pago.lift()
    window_pago.focus_force()
    window_pago.grab_set()
    window_pago.resizable(False, False)

    def CambioEntregado(event):
        total = calculate_total
        Frecibido = entry_recibido.get()
        try:
            recibido = float(Frecibido) 
            if (recibido) < total:  
                messagebox.showerror("ERROR", "El valor ingresado no puede ser 0 o menor al total")
                return
            else:               
                vuelto = recibido - float(total)
                lbl_vuelto.configure(text = f"${vuelto:,.2f}")
        except ValueError as va:
            messagebox.showerror("Entrada invalida", "Ingrese un numero valido")
    
    # Encabezado
    headerPagos = ctk.CTkLabel(
        window_pago,
        text="Confirmacion del Pago\nSelecciona el metodo de pago ",
        font=ctk.CTkFont(size=16, weight="bold"),
        text_color=colores.get('texto'),
        justify="center"
    )
    headerPagos.pack(pady=(20, 10))

    # Marco de items
    marco_items = ctk.CTkScrollableFrame(
        window_pago,
        fg_color=colores.get('tarjeta'),
        label_text="Orden completa"
    )   
    marco_items.pack(fill="both", expand=True, padx=20, pady=10)

    # Poblamos los items en el toplevel
    if not order_items:
        ctk.CTkLabel(marco_items, text="No hay items en la orden.", text_color=colores.get('texto')).pack(pady=20)
    else:
        for name, data in order_items.items():
            ctk.CTkLabel(marco_items, text=f"{name} x{data['cantidad']}  -  ${data['precio']*data['cantidad']:.2f}", text_color=colores.get('texto')).pack(anchor='w', padx=10, pady=4)

# CONTENEDOR PRINCIPAL para las opciones de pago y totales
    contenedor_opciones = ctk.CTkFrame(window_pago, fg_color="transparent")
    contenedor_opciones.pack(padx=20, pady=20, fill="x")

    paymentFrame = ctk.CTkFrame(contenedor_opciones, fg_color=colores.get('tarjeta'))
    paymentFrame.pack(side="left", padx=(0, 20), pady=0, anchor="n") 

    metodo_pago = ctk.StringVar(value="Cash")
    ctk.CTkLabel(paymentFrame, text="Método de Pago:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", padx=10, pady=(10, 5))
    ctk.CTkRadioButton(paymentFrame, text="Efectivo", variable=metodo_pago, value="Cash").pack(anchor="w", padx=10, pady=5)
    ctk.CTkRadioButton(paymentFrame, text="Tarjeta", variable=metodo_pago, value="Card").pack(anchor="w", padx=10, pady=5)

    #Totales(Marco Derecho)
    total_frame = ctk.CTkFrame(contenedor_opciones, fg_color=colores.get('tarjeta'))    
    total_frame.pack(side="left", padx=(20, 0), pady=0, anchor="n")
    total_frame.grid_columnconfigure(0, weight=1) # Columna de Etiquetas (Total a pagar)
    total_frame.grid_columnconfigure(1, weight=1)
    
    ctk.CTkLabel(total_frame, text="Total a pagar:", font=ctk.CTkFont(size=14, weight="bold")).grid(row=0, column=0, sticky="w", padx=10, pady=10)
    lbl_total = ctk.CTkLabel(total_frame, text=f"${calculate_total}", font=ctk.CTkFont(size=14)) 
    lbl_total.grid(row=0, column=1, sticky="e", padx=10, pady=10)

    ctk.CTkLabel(total_frame, text="Total recibido:", font=ctk.CTkFont(size=14, weight="bold")).grid(row=1, column=0, sticky="w", padx=10, pady=10)
    entry_recibido = ctk.CTkEntry(total_frame, placeholder_text="Monto", width=120)
    entry_recibido.grid(row=1, column=1, sticky="e", padx=10, pady=10)

    ctk.CTkLabel(total_frame, text="Vuelto a dar:", font=ctk.CTkFont(size=14, weight="bold")).grid(row=2, column=0, sticky="w", padx=10, pady=10)
    lbl_vuelto = ctk.CTkLabel(total_frame, text="$0.00", font=ctk.CTkFont(size=14))
    lbl_vuelto.grid(row=2, column=1, sticky="e", padx=10, pady=10)

    #Evento para calcular vuelto al ingresar monto recibido
    entry_recibido.bind("<Return>",  CambioEntregado)

    lbl_mainpago = ctk.CTkLabel(
        window_pago,
        text="¿Deseas confirmar el pago?",
        font=ctk.CTkFont(size=16, weight="bold")
    )
    lbl_mainpago.pack(pady=20)

    botones_pagos = ctk.CTkFrame(window_pago)
    botones_pagos.pack(pady=10)

    def confirmar_pago():
        #Recuperar fecha del sistema
        fecha = datetime.now()
        fecha_actual = fecha.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        #Cliente: Publico General
        IdCliente = 1
        IdEmpleado = usuario.sesion_actual
        TotalVenta = calculate_total

        detalle_lista = []        
        for name, data in order_items.items():
            try:
                nombre = controlProducto.ObtenerId(name)
            except Exception:
                messagebox.showerror("Error","El Producto no es valido")
                return
            detalle_lista.append((nombre[0], data['cantidad']))
            
        #Verificar si el stock es suficiente antes de confirmar la venta
        stock = controlProducto.BuscarProducto(nombre[0])[3]
        if stock < data['cantidad']:
            messagebox.showerror("error", "stock insficiente")
        else:
            print(f"fecha: {fecha_actual} \nIdCliente: {IdCliente} \nIdEmpleado: {IdEmpleado} \nDetallesVenta {detalle_lista} \nTotalVenta: {TotalVenta}")
            v = Venta(TotalVenta, fecha_actual, IdCliente, IdEmpleado)
            serviceVenta.AgregarVentaCompleta(v,detalle_lista)
            # Intentar refrescar reportes en el dashboard si está disponible
            try:
                root = vista_menu.winfo_toplevel()
                dashboard = getattr(root, 'dashboard', None)
                if dashboard:
                    reports_frame = dashboard.views.get('reports')
                    if reports_frame and hasattr(reports_frame, 'refresh_reports'):
                        reports_frame.refresh_reports()
            except Exception as e:
                print(f"Advertencia: no se pudo refrescar reportes: {e}")

        order_items.clear()
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
    
    return WindowPago