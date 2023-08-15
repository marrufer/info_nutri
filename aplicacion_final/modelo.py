"""
Este modulo contiene las funciones que hacen de nexo entre la vista y la base
de datos.
"""
#Importacion de las clases y funciones a utilizar
import socket
from peewee import *
from gestion_base import Datos
from observador import Sujeto
from verificacion_datos import variables_vacias,regex
from decoradores import decorador_modelo

#Creacion de la base de datos:

class Abmc(Sujeto):  
    def consulta(self,tree):
        #Eliminacion de elementos del treeview
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        for fila in  Datos.select():
            tree.insert("", 0, text = fila.mi_id, values = (fila.nombre, fila.informacion_general, fila.sodio))
        #Si todavia no hay elementos guardados en la base se eleva una excepcion para que
        #la vista le avise al usuario.
        if len(Datos.select()) == 0:
            raise Exception()
    #el metodo alta tiene un observador:
    def alta(self,tree,var_nombre,var_info_gral,var_sodio):
        variables_vacias(var_nombre,var_info_gral,var_sodio)
        regex(var_nombre)
        #Si ambas condiciones se cumplen, se ejecuta el metodo 'guardar_bd' de Conexion 
        #para guardar los nuevos datos en la base.
        producto = Datos()
        producto.nombre=var_nombre.get()
        producto.informacion_general=var_info_gral.get()
        producto.sodio=var_sodio.get()
        producto.save()
        #Observador
        self.notificar(self.alta.__name__,var_nombre.get(), var_info_gral.get(),var_sodio.get())
        #envio datos de alta al servidor
        HOST, PORT = "localhost", 9999
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        datos_alta=var_nombre.get()+"\n"+var_info_gral.get()+"\n"+var_sodio.get()+"\n"+"alta"
            
        sock.sendto(datos_alta.encode("UTF-8"), (HOST, PORT))
        received = sock.recvfrom(1024)        
        print(received )
        #Actualizar treeview
        self.consulta(tree)
    #los metodos baja y modificar tienen decoradores
    @decorador_modelo
    def baja(self,tree,valor):
        #Se obtiene el id del elemento seleccionado del treeview
        item = tree.item(valor)
        valor_id = item['text']
        borrar = Datos.get(Datos.mi_id==valor_id)
        borrar.delete_instance()     
        tree.delete(valor)
    @decorador_modelo
    def modificar(self,tree,var_nombrem,var_info_gralm,var_sodiom):
        #En este caso la condicion es que las variables tengan un valor para guardar 
        #los cambios realizados.
        variables_vacias(var_nombrem,var_info_gralm,var_sodiom)
        #Se toma el id del elemento que se quiere modificar, es decir el que se selecciona
        # en el treeview.
        valor = tree.selection()
        item = tree.item(valor)
        valor_id = item['text']
        
        actualizar = Datos.update(nombre=var_nombrem.get(),
                                informacion_general=var_info_gralm.get(),
                                sodio=var_sodiom.get(),
                                ).where(Datos.mi_id == valor_id)
        actualizar.execute()
        self.consulta(tree)          
       
    

