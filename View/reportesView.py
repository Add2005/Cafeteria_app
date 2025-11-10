import customtkinter as ctk
import matplotlib.pyplot as plt
from PIL import Image
from Controller.reporte_controller import ReporteController

def crear_vista_reportes(parent, colores):    
    vista = ctk.CTkFrame(parent, fg_color=colores.get('principal'))
    vista.grid(row=0, column=0, sticky="nsew")
    # permitir que la vista se expanda con el contenedor
    vista.grid_rowconfigure(1, weight=1)
    vista.grid_columnconfigure(0, weight=1)

    lblTitulo = ctk.CTkLabel(vista, text="Reportes",
                             font=ctk.CTkFont(size=24, weight="bold"),
                            text_color=colores.get('texto'))
    lblTitulo.place(x=20, y=20)

    # Contenedor principal que debe crecer con la ventana (aquí colocaremos el scrollable frame)
    content_frame = ctk.CTkFrame(vista, fg_color="transparent")
    content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # ScrollFrame para los reportes (dentro del content_frame para que crezca)
    scroll_frame = ctk.CTkScrollableFrame(content_frame, fg_color=colores.get('principal'))
    scroll_frame.grid(row=0, column=0, sticky="nsew")

    lblRporteMes = ctk.CTkLabel(scroll_frame, text="Reporte de ventas mensuales",
                                font=ctk.CTkFont(size=18, weight="bold"),
                                text_color=colores.get('texto'))
    lblRporteMes.pack(anchor="w", pady=(10, 5), padx=10)

    # Marco para el reporte mensual (consistente con otras vistas)
    frame_reporte_mes = ctk.CTkFrame(scroll_frame, fg_color=colores.get('tarjeta'))
    frame_reporte_mes.pack(fill="both", expand=True, padx=10, pady=(0, 20))
    frame_reporte_mes.grid_columnconfigure(0, weight=1)

    # placeholder para la imagen del reporte mensual (será actualizada por refresh_reports)
    label_imagen = ctk.CTkLabel(frame_reporte_mes, image=None, text="")
    label_imagen.pack(fill="both", expand=True, padx=10, pady=10)

    #Productos mas vendidos
    lblRporteProductos = ctk.CTkLabel(scroll_frame, text="Productos mas vendidos",
                                font=ctk.CTkFont(size=18, weight="bold"),
                                text_color=colores.get('texto'))
    lblRporteProductos.pack(anchor="w", pady=(10, 5), padx=10)

    # Marco para el reporte de productos (consistente con otras vistas)
    frame_reporte_productos = ctk.CTkFrame(scroll_frame, fg_color=colores.get('tarjeta'))
    frame_reporte_productos.pack(fill="both", expand=True, padx=10, pady=(0, 20))
    frame_reporte_productos.grid_columnconfigure(0, weight=1)

    # placeholder para la imagen del reporte de productos
    label_imagen_productos = ctk.CTkLabel(frame_reporte_productos, image=None, text="")
    label_imagen_productos.pack(fill="both", expand=True, padx=10, pady=10)

    # función para generar/actualizar los reportes (se puede llamar externamente)
    def refresh_reports():
        try:
            controller = ReporteController()

            # Ventas mensuales
            reportes = controller.ObtenerVentasMensuales()
            meses = [f'Mes {row[0]}' for row in reportes]
            ventas = [row[2] for row in reportes]

            plt.figure(figsize=(8, 4.5))
            plt.bar(meses, ventas, color=colores.get('secundario'))
            plt.title("Ventas Mensuales")
            plt.xlabel("Meses")
            plt.ylabel("Ventas ($)")
            plt.tight_layout()
            plt.savefig("imgs/reporte_mensual.png")
            plt.close()

            imagen = ctk.CTkImage(Image.open("imgs/reporte_mensual.png"), size=(700, 400))
            label_imagen.configure(image=imagen)
            label_imagen.image = imagen

            # Productos mas vendidos
            productos_data = controller.ObtenerProductosMasVendidos()
            productos = [row[1] for row in productos_data]
            cantidades = [row[2] for row in productos_data]

            plt.figure(figsize=(8, 4.5))
            plt.pie(cantidades if cantidades else [1], labels=productos if productos else ['N/A'], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
            plt.title("Productos Mas Vendidos")
            plt.tight_layout()
            plt.savefig("imgs/reporte_productos.png")
            plt.close()

            imagen_productos = ctk.CTkImage(Image.open("imgs/reporte_productos.png"), size=(700, 400))
            label_imagen_productos.configure(image=imagen_productos)
            label_imagen_productos.image = imagen_productos
        except Exception as e:
            print(f"Error actualizando reportes: {e}")

    # Exponer la función de refresco en el frame para que otras vistas la invocen
    vista.refresh_reports = refresh_reports

    # generar los reportes inicialmente
    refresh_reports()

    return vista
