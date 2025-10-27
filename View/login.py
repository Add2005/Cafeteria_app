import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginView:
    def __init__(self, controller=None):
        self.root = ctk.CTk()
        self.root.title("Login - Cafeteria")
        self.root.geometry("1000x650")
        self.root.resizable(0,0)
        
        frame_left = ctk.CTkFrame(self.root, width=430, height=620, corner_radius=10)
        frame_left.place(x=25, y=15)
        
          #imagen de bg en el frame izqu
        image = ctk.CTkImage(Image.open("imgs/bg.jpg"), size=(400, 600))
        label_image = ctk.CTkLabel(frame_left, image=image, text="")
        label_image.place(x=15, y=10)
        
        frame_login = ctk.CTkFrame(self.root, width=400, height=500, corner_radius=10)
        frame_login.place(relx=0.53, rely=0.5, anchor="w")
        #Try para que el frame no se redimensione al agregar widgets
        try:
            frame_login.pack_propagate(False)
        except Exception:
            pass
        
        label_titulo = ctk.CTkLabel(frame_login, text="Iniciar Sesion", font=ctk.CTkFont(size=24, weight="bold"))
        label_titulo.pack(pady=(40, 20))

        #Entradas como atributos para que los handlers puedan acceder a ellas
        self.entry_usuario = ctk.CTkEntry(frame_login, placeholder_text="Usuario", width=300, height=40)
        self.entry_usuario.place(y=150, x=50)
        self.entry_contra = ctk.CTkEntry(frame_login, placeholder_text="Contraseña", width=300, height=40, show="*")
        self.entry_contra.place(y=220, x=50)

        btn_registrarse = ctk.CTkButton(frame_login, text="Registrarse", width=100, height=30)
        btn_registrarse.place(y=290, x=150)
        boton_entrar = ctk.CTkButton(frame_login, text="Entrar", width=200, height=40, command=self._on_entrar)
        boton_entrar.place(y=340, x=100)

        # Controller opcional: puede ser pasado en el constructor o seteado despues
        self.controller = controller
    
    
    def mostrar(self):
        self.root.mainloop()

    #funcion para setear el controller despues de instanciar la vista
    def set_controller(self, controller):
        self.controller = controller

    def mostrar_mensaje(self, texto: str, tipo: str = "info"):
        if tipo == "error":
            messagebox.showerror("Error", texto)
        else:
            messagebox.showinfo("Informacion", texto)

    def cerrar(self):
        try:
            self.root.destroy()
        except Exception:
            pass

    def _on_entrar(self):
        #cuando se presione el btn entrar se llama a on_login del controller
        if not self.controller:
            messagebox.showerror("Error", "Controlador no configurado")
            return

        username = self.entry_usuario.get().strip()
        password = self.entry_contra.get().strip()
        #el controller se encargara de abrir el dashboard
        try:
            self.controller.on_login(username, password)
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar el login: {e}")