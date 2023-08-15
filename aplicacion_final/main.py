"""
El modulo main.py cumple la funcion de controlador de la aplicacion
desde aqui se lanza la ventana.
"""
#importacion de clases
from tkinter import Tk
from vista import Vista
from observador import ObservadorConcretoA
__author__="Martina Ruiz Ferrate"
__mail__="ruizferratemartina@gmail.com"
__version__="3.5"
class Controller:
    def __init__(self, master):
        self.root_controler = master
        self.objeto_vista = Vista(self.root_controler)
        self.el_observador = ObservadorConcretoA(self.objeto_vista.objeto)


if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)
    root_tk.mainloop()
