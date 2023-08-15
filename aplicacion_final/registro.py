import os
import datetime
import sys
"""
Contiene una clase que se usa para registrar excepciones durante el uso de la aplicación.
"""
#creacion de la clase 'RegistroExcepciones', que permite crear un archivo .txt donde se 
#registran las excepciones que se producen durante el uso de la aplicacion.
#En el registro se indica informacion sobre el tipo de error, archivo en que se produce
#y fecha y hora.
class RegistroExcepciones():
        ruta = os.path.dirname(os.path.abspath(__file__))+"\\log.txt" 
        fecha = datetime.datetime.now()   
        def registrar_error(self,linea,archivo): 
                log = open(self.ruta, 'a') 
                print('Se ha dado un error:',
                        sys.exc_info(),
                        archivo, 
                        linea,
                        self.fecha,
                        file=log
                        )