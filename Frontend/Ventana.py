from customtkinter import *
from PIL import Image, ImageTk
import sys  

import Loggin

class Ventana():

    def __init__(self):

        self.app = CTk()
        self.Ancho = self.obtenerAncho(self.app, 60)
        self.Largo = self.obtenerLargo(self.app, 60)
        self.Loggin = False

        self.app.geometry(f"{self.Ancho}x{self.Largo}")
        self.app.title("SGBD Jalisco")

        #Paleta de Colores

        self.colorFondo = '#373739'
        self.primerGris = "#19191a"
        self.segundoGris = "#19191a"
        self.textoGris = "#c6c6c6"
        self.posicionComandos = 1

        #Dimensiones de mis Contenedores

        self.primerFrameAncho = None
        self.primerFrameLargo = None

        self.segundoFrameAncho = None
        self.segundoFrameLargo = None

        self.segundoPrimerFrameAncho = None
        self.segundoPrimerFrameLargo = None

        self.segundoSegundoFrameAncho = None
        self.segundoSegundoFrameLargo = None

        self.tercerFrameAncho = None
        self.tercerFrameLargo = None

        self.establecerFrames(self.app)

        self.app.mainloop()

    def obtenerAncho(self, Ventana, Porcentaje, Ancho = None):

        if(Ancho == None):

            Ancho = Ventana.winfo_screenwidth()
            return int((Ancho * Porcentaje) / 100)
        
        return int((Ancho * Porcentaje) / 100)

    def obtenerLargo(self, Ventana, Porcentaje, Largo = None):

        if(Largo == None):

            Largo = Ventana.winfo_screenheight()
            return (Largo * Porcentaje) // 100
        
        return (Largo * Porcentaje) // 100
    
    def obtenerAnchoWidget(self, Widget, Porcentaje, Ancho = None):
        
        if(Ancho == None):

            Ancho = Widget.winfo_reqwidth()
            return (Ancho * Porcentaje) // 100
        
        return (Ancho * Porcentaje) // 100
    
    def obtenerLargoWidget(self, Widget, Porcentaje, Largo = None):
        
        if(Largo == None):

            Largo = Widget.winfo_reqheight()
            return (Largo * Porcentaje) // 100
        
        return (Largo * Porcentaje) // 100

    def establecerFrames(self, Ventana):

        Ventana.columnconfigure(0, weight = 1)
        Ventana.rowconfigure(0, weight = 0)
        Ventana.rowconfigure(1, weight = 1)
        Ventana.rowconfigure(2, weight = 1)

        #Primer Widget Principal

        self.primerFrameAncho = self.obtenerAncho(Ventana, 100, self.Ancho)
        self.primerFrameLargo = self.obtenerLargo(Ventana, 5, self.Largo)

        primerFrame = CTkFrame(master=Ventana, fg_color= self.primerGris, 
                               width = self.primerFrameAncho,
                               height = self.primerFrameLargo)
        primerFrame.grid(row = 0, column = 0, sticky="nswe")

        self.establecerNavegacion(primerFrame)

        self.segundoFrameAncho = self.obtenerAncho(Ventana, 100, self.Ancho)
        self.segundoFrameLargo = self.obtenerLargo(Ventana, 60, self.Largo)

        #Segundo Widget Principal

        segundoFrame = CTkFrame(master=Ventana, fg_color= self.colorFondo, 
                               width =  self.segundoFrameAncho,
                               height = self.segundoFrameLargo)
        segundoFrame.grid(row = 1, column = 0, sticky="nswe")

        #SubWidgets del Segundo Widget Principal

        segundoFrame.columnconfigure(0, weight=1)
        segundoFrame.columnconfigure(1, weight=1)
        segundoFrame.rowconfigure(0, weight=1)

        #Barra Lateral Izquierda

        self.segundoPrimerFrameAncho = self.obtenerAnchoWidget(segundoFrame, 30)
        self.segundoPrimerFrameLargo = self.obtenerLargoWidget(segundoFrame, 100)
        
        segundoPrimerFrame = CTkFrame(master=segundoFrame, fg_color= self.primerGris, 
                               width = self.segundoPrimerFrameAncho,
                               height = self.segundoPrimerFrameLargo,
                               corner_radius=0)
        segundoPrimerFrame.grid(row = 0, column = 0, sticky="nswe")

        #segundoPrimerFrame.grid_propagate(False) 

        self.listasDatos(segundoPrimerFrame)

        #Segemento Derecho (Display)
        
        self.segundoSegundoFrameAncho = self.obtenerAnchoWidget(segundoFrame, 70)
        self.segundoSegundoFrameLargo = self.obtenerLargoWidget(segundoFrame, 100)

        segundoSegundoFrame = CTkFrame(master=segundoFrame, fg_color=self.colorFondo, 
                               width = self.segundoSegundoFrameAncho,
                               height = self.segundoSegundoFrameLargo,
                               corner_radius=0)
        segundoSegundoFrame.grid(row = 0, column = 1, sticky="nswe")
        #segundoSegundoFrame.grid_propagate(False) 

        self.graficoPredeterminado(segundoSegundoFrame)

        #Tercer widget Principal

        self.tercerFrameAncho = self.obtenerAncho(Ventana, 100, self.Ancho)
        self.tercerFrameLargo = self.obtenerLargo(Ventana, 35, self.Largo)
    
        tercerFrame = CTkFrame(master=Ventana, fg_color=self.segundoGris, 
                               width =  self.tercerFrameAncho,
                               height = self.tercerFrameLargo,
                               corner_radius = 0,
                               border_color="White",
                               border_width= 1,)
        tercerFrame.grid(row = 2, column = 0, sticky="nswe")

        tercerFrame.columnconfigure(0, weight=1)
        tercerFrame.rowconfigure(0, weight=1)
        self.terminal(tercerFrame)

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

       loggin = CTkButton(Frame, text="Loggin", corner_radius=0, command = lambda : self.loggin(self.app))
       loggin.grid(row=0, column=2, sticky = "e")

    def listasDatos(self, Frame):

        Frame.rowconfigure(0, weight = 1)
        Frame.rowconfigure(1, weight = 1)
        Frame.columnconfigure(0, weight = 1) 

        Imagen = CTkImage(light_image=Image.open("Imagenes/basesDatos.png"),
                          dark_image=Image.open("Imagenes/basesDatos.png"),
                          size = (16, 16))
        

        Texto = CTkLabel(master = Frame,
                                         text = "  Lista Datos  ",
                                         text_color = self.textoGris,   
                                         corner_radius = 0, 
                                         width = self.obtenerAnchoWidget(Frame, 100, self.segundoPrimerFrameAncho),
                                         height = self.obtenerLargoWidget(Frame, 10, self.segundoPrimerFrameLargo),
                                         image=Imagen,
                                         compound = "left",
                                        )
        

        Texto.grid(row = 0, column = 0,  sticky="new") 

    def graficoPredeterminado(self, Frame):

        print(Frame)

        Frame.rowconfigure(0, weight = 1)
        Frame.columnconfigure(0, weight = 1)

        Imagen = CTkImage(light_image = Image.open("Imagenes/Stock.png"), 
                          dark_image = Image.open("Imagenes/Stock.png"),
                          size=(self.obtenerLargoWidget(Frame, 50), self.obtenerLargoWidget(Frame, 50)))
        
        Texto = CTkLabel(master = Frame,
                                         text = "Selecciona el menu de opciones o interactua con la terminal para analizar datos.",
                                         text_color = self.textoGris,   
                                         corner_radius = 0, 
                                         width = self.obtenerAnchoWidget(Frame, 100, self.segundoSegundoFrameAncho),
                                         height = self.obtenerLargoWidget(Frame, 100, self.segundoSegundoFrameLargo),
                                         wraplength = self.obtenerAnchoWidget(Frame, 100),
                                         image=Imagen,
                                         compound = "top"
                                        )

        Texto.grid(row = 0, column = 0,  sticky="nswe")
   
    def terminal(self, Frame):
                 
        cajaComandos = CTkTextbox(master=Frame,
                                  width = self.obtenerAnchoWidget(Frame, 100, self.tercerFrameAncho),
                                  height = self.obtenerLargoWidget(Frame, 100, self.tercerFrameLargo),
                                  text_color = "White",
                                  font=("consolas", 15))
        
        cajaComandos.grid(row = 0, column = 0, sticky = "nsew")
        
        cajaComandos.insert("1.0", "SGDB Jalisco [Version 1.0]\n\n")
        cajaComandos.insert("3.0", "¡Hola Bienvenido! Escribe help\n\n")
        cajaComandos.insert("5.0", "Usuario>\n")

        self.posicionComandos = 6

        cajaComandos.bind("<Return>", lambda event: self.Enter(event, cajaComandos))

    def Enter(self, event, cajaComandos):

        print(self.posicionComandos)
        comando = cajaComandos.get(f"{self.posicionComandos}.0", "end-1c")
        self.ejecutarComando(cajaComandos, comando)

        cajaComandos.insert(f"{self.posicionComandos}.0", "Usuario>")

        #La caja de comandos responde despues del prompt del cursor, aun falta verificar si es posible mover el cursor hasta el termino del texto previo.

        #cajaComandos.mark_set("insert", f"{self.posicionComandos}.9")

    def ejecutarComando(self, cajaComandos, comando):

        print(comando)

        comandosDisponibles = { "cls" : "Borra toda la terminal",
                               "exit" : "Salir",
                               "restart" : "Reiniciar",}

        if(comando == "help"):

            self.posicionComandos += 1

            for comando, significado in comandosDisponibles.items():

                self.posicionComandos += 1

                cajaComandos.insert(f"{self.posicionComandos}.0", "\n{} : {}".format(comando, significado))

            self.posicionComandos += 1  
            cajaComandos.insert(f"{self.posicionComandos}.0", "\n\n")  
            self.posicionComandos += 1  

        elif(comando == "cls"):

            cajaComandos.delete("1.0", "end")
            self.posicionComandos = 2

        elif(comando == "exit"):

            sys.exit()

        elif(comando == "restart"):
            
            pass

        else:
            
            self.posicionComandos += 3
            cajaComandos.insert(f"{self.posicionComandos}.0", "\nComando '{}' no reconocido.\n\n".format(comando))
            self.posicionComandos += 1

    def loggin(self, Ventana):

        Loggin.Loggin(Ventana)

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

if __name__ == "__main__":
    ventana_principal = Ventana()            
