import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from Controller.login_controller import LoginController
from Entities.usuario import usuario
from View.dashboard import run_dashboard

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def LoginView():
    
    controller = LoginController()
    
    def entrar():
        username = entry_usuario.get().strip()
        password = entry_contra.get().strip()
        try:
            if controller.on_login(username, password):
                Id = controller.RegistrarIdEmpleado(username)
                user = controller.Usuario_Accesado(username)
                usuario.GuardarIdEmpleado(Id)  
                print(f"IdEmpleado: {Id}")
                root.destroy()
                run_dashboard(user)
            else:
                messagebox.showwarning("Cuidado!", "El usuario y/o la contraseña no son correctas")
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar el login: {e}")
            
            
    root = ctk.CTk()
    root.title("Login - Cafeteria")
    root.geometry("1000x650")
    root.resizable(0,0)

    frame_left = ctk.CTkFrame(root, width=430, height=620, corner_radius=10)
    frame_left.place(x=25, y=15)

    #imagen de bg en el frame izqu
    image = ctk.CTkImage(Image.open("imgs/bg.jpg"), size=(400, 600))
    label_image = ctk.CTkLabel(frame_left, image=image, text="")
    label_image.place(x=15, y=10)

    frame_login = ctk.CTkFrame(root, width=400, height=500, corner_radius=10)
    frame_login.place(relx=0.53, rely=0.5, anchor="w")
    #Try para que el frame no se redimensione al agregar widgets
    try:
        frame_login.pack_propagate(False)
    except Exception:
        pass

    label_titulo = ctk.CTkLabel(frame_login, text="Iniciar Sesion", font=ctk.CTkFont(size=24, weight="bold"))
    label_titulo.pack(pady=(40, 20))

    #iconos de usuario y contraseña
    icon_usuario = ctk.CTkImage(Image.open("imgs/usr.png").resize((20, 20)))
    icon_contra = ctk.CTkImage(Image.open("imgs/psw.png").resize((20,20)))

    label_icon_usuario = ctk.CTkLabel(frame_login, image=icon_usuario, text="")
    label_icon_usuario.place(y=155, x=20)
    label_icon_contra = ctk.CTkLabel(frame_login, image=icon_contra, text="")
    label_icon_contra.place(y=225, x=20)

    #Entradas como atributos para que los handlers puedan acceder a ellas
    entry_usuario = ctk.CTkEntry(frame_login, placeholder_text="Usuario", width=275, height=40)
    entry_usuario.place(y=150, x=50)
    entry_contra = ctk.CTkEntry(frame_login, placeholder_text="Contraseña", width=275, height=40, show="*")
    entry_contra.place(y=220, x=50)

    btn_registrarse = ctk.CTkButton(frame_login, text="Registrarse", width=100, height=30)
    btn_registrarse.place(y=290, x=150)
    boton_entrar = ctk.CTkButton(frame_login, text="Entrar", width=200, height=40, command=entrar)
    boton_entrar.place(y=340, x=100)        

    root.mainloop()
    
    return LoginView