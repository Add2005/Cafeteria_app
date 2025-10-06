import customtkinter as ctk

def crear_vista_reportes(parent, colores):
    vista = ctk.CTkFrame(parent, fg_color=colores.get('principal'))
    vista.grid(row=0, column=0, sticky="nsew")
    return vista
