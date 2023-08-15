"""
El modulo verificacion_datos.py contiene las funciones usadas en el modelo para
verificar que los datos ingresados por el usuario sean adecuados.
"""
import re
#'variables_vacias': verifica si las variables del
#formulario estan vacias o son solo espacios en blanco.
def variables_vacias(var_nombre,var_info_gral,var_sodio):
        variables = [var_nombre.get(),
                var_info_gral.get(),
                var_sodio.get()]
        for i in variables:
                assert (len(i)!=0 and i.isspace()!=True),"Se quieren registrar\
                                                         variables vacias"
def regex(var_nombre):
        #Define una variable cadena que es el valor del campo 'nombre' del formulario:
        cadena = var_nombre.get()
        #Define un patron regex que incluye todos los caracteres alfanumericos del 
        #alfabeto español, mayusculas y minusculas y los espacios.
        patron = "^[a-zA-Z0-9 áéíóúñüÁÉÍÓÚÑÜ]*$"
        #Con el modulo re se compara el valor de 'nombre' con el patron, si no coinciden
        #se produce una excepcion.
        if re.match(patron,cadena)==None:
                raise Exception("Valor de nombre no permitido")



        
