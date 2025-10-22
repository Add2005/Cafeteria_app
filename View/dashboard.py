import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from customtkinter import CTkImage

# Appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

# Theme colors (cafeteria / tierra)
COLOR_PRIMARY = "#202332" 
COLOR_SECONDARY = "#323852"  
COLOR_TEXT = "#FFFFFF"      
COLOR_BG_CARD = "#292931"   

# importar las vistas modulares
from View.menuView import crear_vista_menu
from View.historialView import crear_vista_historial
from View.reportesView import crear_vista_reportes

class DashboardView:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Cafeteria - Dashboard")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

        # configuracion de la cuadricula, el sidebar y el contenedor de vistas
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        
        self.nav_width = 80
        self.navigation_frame = ctk.CTkFrame(self.root, width=self.nav_width, corner_radius=0, fg_color=COLOR_BG_CARD)
        self.navigation_frame.grid(row=0, column=0, sticky="ns")
        # mantener el sidebar sin que se expanda horizontalmente
        self.navigation_frame.grid_propagate(False)

        # logo y titulo centrado
        self.logo_label = ctk.CTkLabel(self.navigation_frame, text="☕", font=ctk.CTkFont(size=28, weight="bold"), text_color=COLOR_TEXT)
        self.logo_label.grid(row=0, column=0, pady=(20, 10))

        # cargamos las imagenes de iconos para los botones del menu
        menu_img = None
        if Image is not None and CTkImage is not None:
            try:
                img_path = "imgs/menu.png"
                pil_img = Image.open(img_path).resize((30, 30))
                menu_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(28, 28))
            except Exception:
                menu_img = None

        if menu_img:
            self.menu_icon = menu_img # guardar referencia en self para evitar que el compilador recoja la imagen
            self.nav_button_menu = ctk.CTkButton(self.navigation_frame, image=self.menu_icon, text="", width=48, height=48,
                                                 fg_color=COLOR_BG_CARD, hover_color=COLOR_SECONDARY,
                                                 command=lambda: self.select_frame_by_name("menu"))
        else:
            self.nav_button_menu = ctk.CTkButton(self.navigation_frame, text="erroe al cargar imagen", width=48, height=48,
                                                 fg_color=COLOR_BG_CARD, hover_color=COLOR_SECONDARY,
                                                 command=lambda: self.select_frame_by_name("menu"))
        self.nav_button_menu.grid(row=1, column=0, pady=8, padx= 10)

        histotial_img = None
        if Image is not None and CTkImage is not None:
            try:
                img_path = "imgs/historial.png"
                pil_img = Image.open(img_path).resize((30, 30))
                histotial_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(28, 28))
            except Exception:
                histotial_img = None

        if histotial_img:
            self.history_icon = histotial_img 
            self.nav_button_orders = ctk.CTkButton(self.navigation_frame, image=self.history_icon, text="", width=48, height=48,
                                                   fg_color=COLOR_BG_CARD, hover_color=COLOR_SECONDARY,
                                                   command=lambda: self.select_frame_by_name("orders"))
        else:
            self.nav_button_orders = ctk.CTkButton(self.navigation_frame, text="error al cargar imagen", width=48, height=48,
                                                   fg_color=COLOR_BG_CARD, hover_color=COLOR_SECONDARY,
                                                   command=lambda: self.select_frame_by_name("orders"))
        self.nav_button_orders.grid(row=2, column=0, pady=8, padx= 10)

        reports_img = None
        if Image is not None and CTkImage is not None:
            try:
                img_path = "imgs/reportes.png"
                pil_img = Image.open(img_path).resize((30, 30))
                reports_img = CTkImage(light_image=pil_img, dark_image=pil_img, size=(28, 28))
            except Exception:
                reports_img = None
        
        if reports_img:
            self.history_icon = reports_img 
            self.nav_button_reports = ctk.CTkButton(self.navigation_frame, image=self.history_icon, text="", width=48, height=48,
                                                    fg_color=COLOR_BG_CARD, hover_color=COLOR_SECONDARY,
                                                    command=lambda: self.select_frame_by_name("reports"))
        else:
            self.nav_button_reports = ctk.CTkButton(self.navigation_frame, text="error al cargar imagen", width=48, height=48,
                                                    fg_color=COLOR_BG_CARD, hover_color=COLOR_SECONDARY,
                                                    command=lambda: self.select_frame_by_name("reports"))
        self.nav_button_reports.grid(row=3, column=0, pady=8, padx= 10)


        # separador
        self.navigation_frame.grid_rowconfigure(4, weight=1)
            
        # Icono de configuracion
        self.nav_button_settings = ctk.CTkButton(self.navigation_frame, text="⚙️", width=40, height=40,
                                                 fg_color=COLOR_BG_CARD, hover_color=COLOR_SECONDARY,
                                                command=self.cerrar)
        self.nav_button_settings.grid(row=5, column=0, pady=12)

        # contendor principal
        self.view_container = ctk.CTkFrame(self.root, fg_color=COLOR_PRIMARY)
        self.view_container.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.view_container.grid_rowconfigure(0, weight=1)
        self.view_container.grid_columnconfigure(0, weight=1)

        # diccionario de vistas
        self.views = {}

        # paleta para pasar a las vistas modulares
        paleta = {
            'principal': COLOR_PRIMARY,
            'secundario': COLOR_SECONDARY,
            'texto': COLOR_TEXT,
            'tarjeta': COLOR_BG_CARD,
        }

        # crear vistas y guardarlas en el diccionario
        self.views['menu'] = crear_vista_menu(self.view_container, paleta)
        self.views['orders'] = crear_vista_historial(self.view_container, paleta)
        self.views['reports'] = crear_vista_reportes(self.view_container, paleta)

        # empezar mostrando el menu
        self.select_frame_by_name("menu")

    def cerrar(self):
        respuesta = messagebox.askokcancel("Salir", "Estas seguro que desas salir?")
        if respuesta:
            self.root.destroy()
            
    def select_frame_by_name(self, name: str):
        """muestra la vista solicitada al obtener el frame y elevarlo en el contendor"""
        def set_active(btn):
            btn.configure(fg_color=("gray75", COLOR_BG_CARD))

        def set_inactive(btn):
            btn.configure(fg_color=COLOR_BG_CARD)

        #  reinicar todos
        set_inactive(self.nav_button_menu)
        set_inactive(self.nav_button_orders)
        set_inactive(self.nav_button_reports)

        # activar el boton seleccionada
        if name == "menu":
            set_active(self.nav_button_menu)
        elif name == "orders":
            set_active(self.nav_button_orders)
        elif name == "reports":
            set_active(self.nav_button_reports)

        view = self.views.get(name)
        if view:
            view.grid(row=0, column=0, sticky="nsew")
            view.lift()

    # al dividir en modulos se facilira el mantenimiento :p


def run_dashboard():
    """crear y ejecuatr el mainloop del dashboard"""
    view = DashboardView()
    view.root.mainloop()
    return view


if __name__ == "__main__":
    # permite ejecutar el dashboard directamente
    run_dashboard()

