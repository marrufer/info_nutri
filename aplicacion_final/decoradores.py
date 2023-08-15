import os
import datetime

def decorador_modelo(funcion):
    fecha = datetime.datetime.now()
    ruta=(os.path.dirname(os.path.abspath(__file__))+ "\\reg.txt")
    def envoltura(*args):
        reg=open (ruta ,"a",encoding="utf-8")
        if funcion.__name__=='modificar':
            valor = args[1].selection()
            print("Se ha actualizado un registro.",
                "ID:",
                (args[1].item(valor))['text'],
                "Nombre:",
                args[2].get(),
                "Información general:",
                args[3].get(),
                "Sodio:",
                args[4].get(),
                fecha,
                file=reg
                )
            return funcion(*args)
        elif funcion.__name__=='baja':
            print("Se ha eliminado un registro.",
            "ID:",
            (args[1].item(args[2]))['text'],
            "Nombre:",
            (args[1].item(args[2]))['values'][0],
            "Información general:",
            (args[1].item(args[2]))['values'][1],
            "Sodio:",
            (args[1].item(args[2]))['values'][2],
            fecha,
            file=reg
            )
            return funcion(*args)
    return envoltura
