from customtkinter import *
from PIL import Image, ImageTk
import sys

class Loggin():

    def __init__(self, Ventana):

        self.amarillo = "#ffd422"
        self.azul = "#27438d"
        self.colorFondo = '#19191a'
        
        self.logginAncho = self.obtenerAncho(Ventana, 50)
        self.logginLargo = self.obtenerLargo(Ventana, 50)

        Ventana.rowconfigure(0, weight = 1)
        Ventana.rowconfigure(1, weight = 0)
        Ventana.rowconfigure(2, weight = 0)
        Ventana.columnconfigure(0, weight = 1)
        Ventana.columnconfigure(1, weight = 1)

        for widget in Ventana.winfo_children():

            if isinstance(widget, CTkFrame):
                widget.destroy() 

        self.establecerFrames(Ventana)

    def obtenerAncho(self, Ventana, Proporcion, Ancho = None):

        if(Ancho == None):

            Ancho = Ventana.winfo_width()

        return (Ancho * Proporcion) // 100
        
    def obtenerLargo(self, Ventana, Proporcion, Largo = None):

        if (Largo == None):

            Largo  = Ventana.winfo_height()

        return (Largo * Proporcion) // 100
    
    def establecerFrames(self, Ventana):
        
        primerLoggin = CTkFrame(master = Ventana,
                                fg_color= self.amarillo,
                                width = self.logginAncho,
                                height = self.logginLargo,
                                corner_radius = 0,
                               )
        
        primerLoggin.grid(row = 0, column = 0, sticky = "nsew")

        self.establecerImagen(primerLoggin)

        segundoLoggin = CTkFrame(master = Ventana,
                                fg_color = self.colorFondo,
                                width = self.logginAncho,
                                height = self.logginLargo,
                                corner_radius = 0)
        
        segundoLoggin.grid(row = 0, column = 1, sticky = "nsew")

        self.establecerLoggin(segundoLoggin)

    def establecerImagen(self, Frame):

        Frame.rowconfigure(0, weight = 1)
        Frame.columnconfigure(0, weight = 1)

        Imagen = Image.open("Imagenes/Loggin.png")

        imagenAncho, imagenAlto = Imagen.size

        imagenAlto = (imagenAlto * 40) // 100
        imagenAncho = (imagenAncho * 40) // 100

        ImagenFrame = CTkImage(light_image = Image.open("Imagenes/Loggin.png"), 
                          dark_image = Image.open("Imagenes/Loggin.png"),
                          size=(imagenAncho, imagenAlto)
                          )
        
        imagenContenedor = CTkLabel(master = Frame, text = "",
                                    width = self.logginAncho,
                                    height = self.logginLargo,
                                    image = ImagenFrame, 
                                    compound = "center")
        
        imagenContenedor.grid(row = 0, column = 0, sticky="nsew")

    def establecerLoggin(self, Frame):

        Frame.rowconfigure(0, weight = 1)
        Frame.rowconfigure(1, weight = 1)
        Frame.columnconfigure(0, weight = 1)
         
        primerLogginAncho = self.obtenerAncho(Frame, 100, self.logginAncho)
        primerLogginLargo = self.obtenerLargo(Frame, 30, self.logginLargo)

        segundoLogginAncho = self.obtenerAncho(Frame, 100, self.logginAncho)
        segundoLogginLargo = self.obtenerLargo(Frame, 70, self.logginLargo)

        textoBienvenida = CTkFrame(master = Frame,
                                    fg_color="green",
                                    width = primerLogginAncho,
                                    height = primerLogginLargo,
                                    corner_radius = 0)

        textoBienvenida.grid(row = 0, column = 0, sticky = "nsew")

        self.incorporarBienvenida(textoBienvenida, primerLogginAncho, primerLogginLargo)

        formulario = CTkFrame(master = Frame,
                              fg_color="blue",
                              width = segundoLogginAncho,
                              height = segundoLogginLargo,
                              corner_radius = 0)
                
        formulario.grid(row = 1, column = 0, sticky = "nsew")

    def incorporarBienvenida(self, Frame, Ancho, Largo):

        texto = CTkLabel(master = Frame,
                        text = "texto",
                        width = self.obtenerAncho(Frame, 50, Ancho),
                        height = self.obtenerLargo(Frame, 50, Largo),
                        bg_color="orange")
        
        texto.pack()
