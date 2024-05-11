from customtkinter import *
from PIL import Image

class Loggin():

    def __init__(self, Ventana, Status):

        self.amarillo = "#ffd422"
        self.azul = "#27438d"
        self.colorFondo = '#19191a'

        Status = True

        self.password = []
        
        self.logginAncho = self.obtenerAncho(Ventana, 50)
        self.logginLargo = self.obtenerLargo(Ventana, 50)

        Ventana.rowconfigure(0, weight = 1)
        Ventana.rowconfigure(1, weight = 0)
        Ventana.rowconfigure(2, weight = 0)
        Ventana.columnconfigure(0, weight = 1)
        Ventana.columnconfigure(1, weight = 1)

        for widget in Ventana.winfo_children():

            widget.destroy() 

        self.establecerFrames(Ventana)

        Ventana.mainloop()

    def __del__(self, Frame = None):

        try:

         Ventana = Frame.winfo_toplevel()

        except:
            pass

        Ventana.destroy()

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
        Frame.rowconfigure(1, weight = 2)
        Frame.columnconfigure(0, weight = 1)
         
        primerLogginAncho = self.obtenerAncho(Frame, 100, self.logginAncho)
        primerLogginLargo = self.obtenerLargo(Frame, 10, self.logginLargo)

        segundoLogginAncho = self.obtenerAncho(Frame, 100, self.logginAncho)
        segundoLogginLargo = self.obtenerLargo(Frame, 90, self.logginLargo)

        textoBienvenida = CTkFrame(master = Frame,
                                    fg_color = self.colorFondo,
                                    width = primerLogginAncho,
                                    height = primerLogginLargo,
                                    corner_radius = 0)

        textoBienvenida.grid(row = 0, column = 0, sticky = "nsew")

        self.incorporarBienvenida(textoBienvenida, primerLogginAncho, primerLogginLargo)

        formulario = CTkFrame(master = Frame,
                              fg_color = self.colorFondo,
                              width = segundoLogginAncho,
                              height = segundoLogginLargo,
                              corner_radius = 0)
                
        formulario.grid(row = 1, column = 0, sticky = "nsew")

        self.incorporarFormulario(formulario, segundoLogginAncho, segundoLogginLargo)

    def incorporarBienvenida(self, Frame, Ancho, Largo):

        Frame.rowconfigure(0, weight = 1)
        Frame.rowconfigure(1, weight = 1)
        Frame.columnconfigure(0, weight = 1)

        primerTexto = CTkLabel(master = Frame,
                        fg_color = self.colorFondo,
                        text_color = self.amarillo,       
                        text = "¡Bienvenido!",
                        font = ("Times New Roman", 60),
                        width = self.obtenerAncho(Frame, 100, Ancho),
                        height = self.obtenerLargo(Frame, 75, Largo))
        
        primerTexto.grid(row = 0, column = 0, sticky = "nsew")

        segundoTexto = CTkLabel(master = Frame,
                        fg_color = self.colorFondo,        
                        text = "JALISCO GOBIERNO DEL ESTADO",
                        font = ("Times New Roman", 12),
                        width = self.obtenerAncho(Frame, 100, Ancho),
                        height = self.obtenerLargo(Frame, 25, Largo))
        
        segundoTexto.grid(row = 1, column = 0, sticky = "new")

    def incorporarFormulario(self, Frame, Ancho, Largo):

        Frame.rowconfigure(0, weight = 1)
        Frame.rowconfigure(1, weight = 1)
        Frame.rowconfigure(2, weight = 1)
        Frame.columnconfigure(0, weight = 1)

        contendorAncho = self.obtenerAncho(Frame, 100, Ancho)
        contenedorLargo = self.obtenerLargo(Frame, 33.3, Largo)

        primerContenedor = CTkFrame(master = Frame,
                                    fg_color = self.colorFondo,
                                    width =  contendorAncho,
                                    height =  contenedorLargo)
        
        primerContenedor.grid(row = 0, column = 0, sticky = "nsew")

        self.usuario(primerContenedor, contendorAncho, contenedorLargo)
        
        segundoContenedor = CTkFrame(master = Frame,
                                    fg_color = self.colorFondo,
                                    width =  contendorAncho,
                                    height =  contenedorLargo)

        segundoContenedor.grid(row = 1, column = 0, sticky = "nsew")

        self.clave(segundoContenedor, contendorAncho, contenedorLargo)

        tercerContenedor = CTkFrame(master = Frame,
                                    fg_color = self.colorFondo,
                                    width =  contendorAncho,
                                    height =  contenedorLargo)
        
        self.boton(tercerContenedor, contendorAncho, contenedorLargo, primerContenedor, segundoContenedor)
        
        tercerContenedor.grid(row = 2, column = 0, sticky = "nsew")  

    def usuario(self, Frame, Ancho, Largo):

        Frame.rowconfigure(0, weight = 1)
        Frame.rowconfigure(1, weight = 1)
        Frame.columnconfigure(0, weight = 1)
        
        Imagen = CTkImage(light_image = Image.open("Imagenes/Usuario.png"), 
                          dark_image = Image.open("Imagenes/Usuario.png"),
                          size=(20, 20))

        texto = CTkLabel(master = Frame,
                         text = "Usuario",
                         font = ("Helvetica", 16),
                         width = self.obtenerAncho(Frame, Ancho, 70),
                         height = self.obtenerLargo(Frame, Largo, 15),
                         image = Imagen,
                         compound = "left",
                         anchor = "w")
        
        texto.grid(row = 0, column = 0)

        usuario = CTkEntry(master = Frame,
                          placeholder_text = "Usuario",
                          width = self.obtenerAncho(Frame, Ancho, 70),
                          height = self.obtenerLargo(Frame, Largo, 30),
                          )

        usuario.grid(row = 1, column = 0)

    def clave(self, Frame, Ancho, Largo):

        Frame.rowconfigure(0, weight = 1)
        Frame.rowconfigure(1, weight = 1)
        Frame.columnconfigure(0, weight = 1)
        
        Imagen = CTkImage(light_image = Image.open("Imagenes/Clave.png"), 
                          dark_image = Image.open("Imagenes/Clave.png"),
                          size=(16, 20))

        texto = CTkLabel(master = Frame,
                         text = " Clave",
                         font = ("Helvetica", 16),
                         width = self.obtenerAncho(Frame, Ancho, 70),
                         height = self.obtenerLargo(Frame, Largo, 15),
                         image = Imagen,
                         compound = "left",
                         anchor = "w")
        
        texto.grid(row = 0, column = 0)

        clave = CTkEntry(master = Frame,
                          placeholder_text = "Clave",
                          width = self.obtenerAncho(Frame, Ancho, 70),
                          height = self.obtenerLargo(Frame, Largo, 30),
                          )
        
        clave.bind("<KeyRelease>", lambda event : self.detectarTecla(clave, event, self.password))

        clave.grid(row = 1  , column = 0)

    def detectarTecla(self, contenedor, event, contenido):

        if (event.keysym == "BackSpace"):

            try:  
                del contenido[-1]
            except:
                pass    
        else:

            teclaPresionada = event.char
            contenido.append(teclaPresionada)

        contenidoOculto = "*" * len(contenido)
        contenedor.delete(0, END)
        contenedor.insert(0, contenidoOculto)

    def boton(self, Frame, Ancho, Largo, primerEntry, segundoEntry):

        Frame.rowconfigure(0, weight = 1)
        Frame.columnconfigure(0, weight = 1)

        boton = CTkButton(master = Frame,
                          text = "Iniciar Sesión",
                          font = ("Helvetica", 16),
                          text_color = self.colorFondo,
                          fg_color = self.amarillo,
                          command = lambda : self.mandarInformacion(primerEntry, segundoEntry),
                          width = self.obtenerAncho(Frame, 60, Ancho),
                          height = self.obtenerLargo(Frame, 60, Largo))
        
        boton.grid(row = 0, column = 0)

    def mandarInformacion(self, frameUsuario, frameClave):
        
        Entradas = frameUsuario.winfo_children()[1]
        Clave = frameClave.winfo_children()[1]

        usuario = Entradas.get()
        password = "".join(self.password)

        print(usuario)
        print(password)

        if(usuario == "user" and password == "admin"):

            self.__del__(frameUsuario)

        else:
            
            self.error(Entradas, Clave)
                
    def error(self, Usuario, Clave):

        Usuario.configure(placeholder_text = "Usuario o Clave Incorrecta", 
                          placeholder_text_color = "Red",
                          )
        
        Usuario.bind("<FocusIn>", lambda event: self.restablecerContenedor(Usuario, "Usuario"))

        Clave.configure(placeholder_text = "Usuario o Clave Incorrecta", 
                        placeholder_text_color = "Red",
                        )
        
        Clave.bind("<FocusIn>", lambda event: self.restablecerContenedor(Clave, "Clave"))
        self.password.clear()

    def restablecerContenedor(self, Entry, String):

        Entry.configure(placeholder_text = String, 
                          placeholder_text_color = 'transparent',
                          )
        Entry.unbind("<FocusIn>")        
