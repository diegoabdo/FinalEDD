from tkinter import *

from views.arbol_busqueda_view import ArbolBusquedaView



class Ventana(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # El usuario tendrá 7 opciones a elegir correspondientes a las 7 estructuras
        master.title("Estructuras de Datos")
        master.geometry("400x300")
        master.config(bg="#066163")

        self.config(bg="#066163")

        # Elementos de la ventana principal

        # Textos de la ventana principal
        self.titulo = Label(self, text="Centro Educativo Naciones",
                            font=("rockwell", 15), bg="#066163", fg="white")

        # Elementos del frame


        # Botón iniciar el frame del arbol de busqueda
        self.arbol_busqueda_boton = Button(
            self, text="Arbol de Busqueda",
            command=lambda: self.renderizar(ArbolBusquedaView),

            # Estilos
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )



        # Posicionamos todos los elementos
        self.titulo.grid(row=0, column=0)

        self.arbol_busqueda_boton.grid(row=1, column=0)


    def renderizar(self, view):

        root = Toplevel()

        ventana_view = view(root)
        ventana_view.pack()

        root.mainloop()