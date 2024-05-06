from customtkinter import *
from PIL import Image, ImageTk
import sys

class Loggin():

    def __init__(self, Ventana):

        Ventana.rowconfigure(0, weight = 1)
        Ventana.columnconfigure(0, weight = 1)
        Ventana.columnconfigure(1, weight = 1)

        for widget in Ventana.winfo_children():

            if isinstance(widget, CTkFrame):
                widget.destroy() 

        primerLoggin = CTkFrame(master = Ventana,
                                fg_color="Red",
                                width = self.obtenerAncho(Ventana, 50),
                                height = self.obtenerLargo(Ventana, 50),
                                corner_radius = 0)
        
        primerLoggin.grid(row = 0, column = 0, sticky = "nsew")

        segundoLoggin = CTkFrame(master = Ventana,
                                fg_color="Blue",
                                width = self.obtenerAncho(Ventana, 50),
                                height = self.obtenerLargo(Ventana, 50),
                                corner_radius = 0)
        
        segundoLoggin.grid(row = 0, column = 1, sticky = "nsew")

    def obtenerAncho(self, Ventana, Proporcion):

        Ancho = Ventana.winfo_width()

        return (Ancho * Proporcion) // 100
        
    
    def obtenerLargo(self, Ventana, Proporcion):

        Largo  = Ventana.winfo_height()

        return (Largo * Proporcion) // 100
