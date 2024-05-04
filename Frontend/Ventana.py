from customtkinter import *
import sys  

class Ventana():

    def __init__(self):

        app = CTk()
        self.Ancho = self.obtenerAncho(app, 60)
        self.Largo = self.obtenerLargo(app, 60)
        self.Loggin = False
        self.colorFondo = '#373739'
        self.primerGris = "#19191a"
        self.segundoGris = "#19191a"

        app.geometry(f"{self.Ancho}x{self.Largo}")

        self.establecerFrames(app)

        app.mainloop()

    def obtenerAncho(self, Ventana, Porcentaje, Ancho = None):

        if(Ancho == None):

            Ancho = Ventana.winfo_screenwidth()
            return int((Ancho * Porcentaje) / 100)
        
        return int((Ancho * Porcentaje) / 100)

    def obtenerLargo(self, Ventana, Porcentaje, Largo = None):

        if(Largo == None):

            Largo = Ventana.winfo_screenheight()
            return int((Largo * Porcentaje) / 100)
        
        return int((Largo * Porcentaje) / 100)
    
    def obtenerAnchoWidget(self, Widget, Porcentaje, Ancho = None):
        
        if(Ancho == None):

            Ancho = Widget.winfo_reqwidth()
            return int((Ancho * Porcentaje) / 100)
        
        return int((Ancho * Porcentaje) / 100)
    
    def obtenerLargoWidget(self, Widget, Porcentaje, Largo = None):
        
        if(Largo == None):

            Largo = Widget.winfo_reqheight()
            return int((Largo * Porcentaje) / 100)
        
        return int((Largo * Porcentaje) / 100)

    def establecerFrames(self, Ventana):

        Ventana.columnconfigure(0, weight = 1)
        Ventana.rowconfigure(0, weight = 0)
        Ventana.rowconfigure(1, weight = 1)
        Ventana.rowconfigure(2, weight = 1)

        #Primer Widget Principal

        primerFrame = CTkFrame(master=Ventana, fg_color= self.primerGris, 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 5, self.Largo),)
        primerFrame.grid(row = 0, column = 0, sticky="nswe")

        self.establecerNavegacion(primerFrame)

        #Segundo Widget Principal

        segundoFrame = CTkFrame(master=Ventana, fg_color= self.colorFondo, 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 65, self.Largo))
        segundoFrame.grid(row = 1, column = 0, sticky="nswe")

        #SubWidgets del Segundo Widget Principal

        segundoFrame.columnconfigure(0, weight=1)
        segundoFrame.columnconfigure(1, weight=0)
        segundoFrame.columnconfigure(2, weight=1)
        segundoFrame.rowconfigure(0, weight=1)
        segundoFrame.update()
        
        segundoPrimerFrame = CTkFrame(master=segundoFrame, fg_color= self.primerGris, 
                               width = self.obtenerAnchoWidget(segundoFrame, 24),
                               height = self.obtenerLargoWidget(segundoFrame, 100),
                               corner_radius=0)
        segundoPrimerFrame.grid(row = 0, column = 0, sticky="nswe")

        """"

        segundoPrimerBorde = CTkFrame(master=segundoFrame, fg_color= self.primerGris, 
                               width = self.obtenerAnchoWidget(None, 100, 2),
                               height = self.obtenerLargoWidget(segundoFrame, 100),
                               corner_radius=0,
                               border_color="White",
                               border_width= 1)
        segundoPrimerBorde.grid(row = 0, column = 1, sticky="nswe")

        """

        segundoSegundoFrame = CTkFrame(master=segundoFrame, fg_color=self.colorFondo, 
                               width = self.obtenerAnchoWidget(segundoFrame, 74),
                               height = self.obtenerLargoWidget(segundoFrame, 100),
                               corner_radius=0,)
        segundoSegundoFrame.grid(row = 0, column = 2, sticky="nswe")

        #Tercer widget Principal
    
        tercerFrame = CTkFrame(master=Ventana, fg_color=self.segundoGris, 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 30, self.Largo),
                               corner_radius = 0,
                               border_color="White",
                               border_width= 1,)
        tercerFrame.grid(row = 2, column = 0, sticky="nswe")

        tercerFrame.columnconfigure(0, weight=1)
        tercerFrame.rowconfigure(0, weight=1)

        cajaComandos = CTkTextbox(master=tercerFrame,
                                  width = self.obtenerAnchoWidget(tercerFrame, 100),
                                  height = self.obtenerLargoWidget(tercerFrame, 100),
                                  text_color = "White",
                                  font=("consolas", 15))
        
        cajaComandos.grid(row = 0, column = 0, sticky = "nsew")
        
        cajaComandos.insert("0.0", "SGDB Jalisco [Version 1.0]\n\n")
        cajaComandos.insert("3.0", "¡Hola Bienvenido! Escribe /help\n\n")
        cajaComandos.insert("5.0", "Usuario> ")

    def establecerNavegacion(self, Frame):
        
       Frame.rowconfigure(0, weight=0)
       Frame.columnconfigure(0, weight=0)
       Frame.columnconfigure(1, weight=1)
       Frame.columnconfigure(2, weight=1)

       valores = ["Opciones", "Diagramas", "Regresiones", "Intervalos Confianza", "Importar", "Exportar" , "Salir"]

       primerAjuste = CTkOptionMenu(Frame, values=valores, corner_radius=0, command=lambda selection: self.opcionesMenu(selection))
       primerAjuste.grid(row = 0, column = 0, sticky = "e")

       Usuario = CTkLabel(Frame, text="Usuario   ", anchor="e")
       Usuario.grid(row=0, column=1, sticky = "ew")

       loggin = CTkButton(Frame, text="Loggin", corner_radius=0)
       loggin.grid(row=0, column=2, sticky = "e")

    def opcionesMenu(self, opcion):
        
        if "Diagramas" == opcion:

            pass

        elif "Regresiones" == opcion:

            pass

        elif "Intervalos Confianza" == opcion:

            pass

        elif "Importar" == opcion:

            pass

        elif "Exportar" == opcion:

            pass

        elif "Salir" == opcion:

            sys.exit()

        else:

            print("Caso no Definido")               
