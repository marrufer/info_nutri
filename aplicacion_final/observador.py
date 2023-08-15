import os
import datetime


class Sujeto():
    observadores=[]
    def agregar(self,obj):
        self.observadores.append(obj)
    def quitar(self, obj):
        self.observadores.pop(obj)
    def notificar(self,*args):
        for observador in self.observadores:
            observador.update(args)

class Observador():
    def update(self):
        raise NotImplementedError("Delegación de actualización")
    
class ObservadorConcretoA(Observador,Sujeto):
    def __init__(self, obj):
        self.observador_a = obj
        self.observador_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        print("Función: ",args[0][0]," Parámetros: ", args[0][1:])
        fecha = datetime.datetime.now()
        ruta=(os.path.dirname(os.path.abspath(__file__))+ "\\reg.txt")
        reg=open(ruta ,"a",encoding="utf-8")
        print("Actualizacion desde ObservadorConcretoA. Se ha ingresado un nuevo producto. ",
                    "Nombre:",
                    args[0][1],
                    "Informacion general:",
                    args[0][2],
                    "Sodio:",
                    args[0][3],
                    fecha,
                    file=reg
                    )