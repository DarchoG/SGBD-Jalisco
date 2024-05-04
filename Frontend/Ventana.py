from customtkinter import *
import sys  

class Ventana():

    def __init__(self):

        app = CTk()
        self.Ancho = self.obtenerAncho(app, 60)
        self.Largo = self.obtenerLargo(app, 60)

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

        primerFrame = CTkFrame(master=Ventana, fg_color="red", 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 5, self.Largo))
        primerFrame.grid(row = 0, column = 0, sticky="nswe")

        self.establecerNavegacion(primerFrame)

        #Segundo Widget Principal

        segundoFrame = CTkFrame(master=Ventana, fg_color="green", 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 65, self.Largo))
        segundoFrame.grid(row = 1, column = 0, sticky="nswe")

        #SubWidgets del Segundo Widget Principal

        segundoFrame.columnconfigure(0, weight=1)
        segundoFrame.columnconfigure(1, weight=1)
        segundoFrame.rowconfigure(0, weight=1)
        segundoFrame.update()
        
        segundoPrimerFrame = CTkFrame(master=segundoFrame, fg_color="black", 
                               width = self.obtenerAnchoWidget(segundoFrame, 25),
                               height = self.obtenerLargoWidget(segundoFrame, 100))
        segundoPrimerFrame.grid(row = 0, column = 0, sticky="nswe")

        segundoSegundoFrame = CTkFrame(master=segundoFrame, fg_color="white", 
                               width = self.obtenerAnchoWidget(segundoFrame, 75),
                               height = self.obtenerLargoWidget(segundoFrame, 100))
        segundoSegundoFrame.grid(row = 0, column = 1, sticky="nswe")

        #Tercer widget Principal
    
        tercerFrame = CTkFrame(master=Ventana, fg_color="blue", 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 30, self.Largo))
        tercerFrame.grid(row = 2, column = 0, sticky="nswe")

    def establecerNavegacion(self, Frame):
        
       Frame.rowconfigure(0, weight=0)
       Frame.columnconfigure(0, weight=0)
       Frame.columnconfigure(1, weight=0)
       Frame.columnconfigure(2, weight=0)

       valores = ["Opciones", "Diagramas", "Regresiones", "Intervalos Confianza", "Importar", "Exportar" , "Salir"]

       primerAjuste = CTkOptionMenu(Frame, values=valores, corner_radius=0, command=lambda selection: self.opcionesMenu(selection))
       primerAjuste.grid(row = 0, column = 0, sticky = "e")

       Usuario = CTkLabel(Frame, text="Usuario   ")
       Usuario.grid(row=0, column=1, sticky = "e")

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
