from customtkinter import *  

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
    
    def establecerFrames(self, Ventana):

        Ventana.columnconfigure(0, weight = 1)
        Ventana.rowconfigure(0, weight = 0)
        Ventana.rowconfigure(1, weight = 1)
        Ventana.rowconfigure(2, weight = 1)

        primerFrame = CTkFrame(master=Ventana, fg_color="red", 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 5, self.Largo))
        primerFrame.grid(row = 0, column = 0, sticky="nswe")

        segundoFrame = CTkFrame(master=Ventana, fg_color="green", 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 70, self.Largo))
        segundoFrame.grid(row = 1, column = 0, sticky="nswe")

        tercerFrame = CTkFrame(master=Ventana, fg_color="blue", 
                               width = self.obtenerAncho(Ventana, 100, self.Ancho),
                               height = self.obtenerLargo(Ventana, 25, self.Largo))
        tercerFrame.grid(row = 2, column = 0, sticky="nswe")
