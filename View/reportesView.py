import customtkinter as ctk
import matplotlib.pyplot as plt
from PIL import Image
from Controller.reporte_controller import ReporteController

def crear_vista_reportes(parent, colores):
    vista = ctk.CTkFrame(parent, fg_color=colores.get('principal'))
    vista.grid(row=0, column=0, sticky="nsew")
    lblTitulo = ctk.CTkLabel(vista, text="Reportes",
                             font=ctk.CTkFont(size=24, weight="bold"),
                            text_color=colores.get('texto'))
    lblTitulo.place(x=20, y=20)
    
    # ScrollFrame para los reportes 
    scroll_frame = ctk.CTkScrollableFrame(vista, width=760, height=500, fg_color=colores.get('principal'))
    scroll_frame.place(x=20, y=70)

    lblRporteMes = ctk.CTkLabel(scroll_frame, text="Reporte de ventas mensuales",
                                font=ctk.CTkFont(size=18, weight="bold"),
                                text_color=colores.get('texto'))
    lblRporteMes.pack(anchor="w", pady=(10, 5), padx=10)

    # Datos de ejemplo para el grafico de la base de datos 
    controller = ReporteController()
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
    label_imagen = ctk.CTkLabel(scroll_frame, image=imagen, text="")
    label_imagen.image = imagen  # mantener referencia para evitar GC 
    label_imagen.pack(padx=10, pady=(0, 20))
    
    #Productos mas vendidos
    lblRporteProductos = ctk.CTkLabel(scroll_frame, text="Productos mas vendidos",
                                font=ctk.CTkFont(size=18, weight="bold"),
                                text_color=colores.get('texto'))
    lblRporteProductos.pack(anchor="w", pady=(10, 5), padx=10)
    
    
    #Datos de prueba para el grafico de productos mas vendidos
    #Grafico de pastel
    controller = ReporteController()
    productos_data = controller.ObtenerProductosMasVendidos()
    productos = [row[1] for row in productos_data]
    cantidades = [row[2] for row in productos_data]
    
    plt.figure(figsize=(8, 4.5))
    plt.pie(cantidades, labels=productos, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
    plt.title("Productos Mas Vendidos")
    plt.tight_layout()
    plt.savefig("imgs/reporte_productos.png")
    plt.close()
    
    imagen_productos = ctk.CTkImage(Image.open("imgs/reporte_productos.png"), size=(700, 400))
    label_imagen_productos = ctk.CTkLabel(scroll_frame, image=imagen_productos, text="")
    label_imagen_productos.image = imagen_productos  # mantener referencia para evitar GC 
    label_imagen_productos.pack(padx=10, pady=(0, 20))
    
    
    return vista
