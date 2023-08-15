
from peewee import *
import pyttsx3
base = SqliteDatabase("informacion_nutricional_server.db")
class BaseModel(Model):
    class Meta:
        database = base
class Datos(BaseModel):
    mi_id = AutoField()
    nombre = CharField()
    informacion_general = CharField()
    sodio = CharField()
   
base.connect()
base.create_tables([Datos])

class Ac():

    engine = pyttsx3.init()

    def alta_servidor(self,data):
        producto = Datos()
        datos_tabla=str(data)
        lista_datos=datos_tabla.split("\n")
        producto.nombre=lista_datos[0]
        producto.informacion_general=lista_datos[1]
        producto.sodio=lista_datos[2]
        producto.save() 
      
       

    def consulta(self,tree):
            records = tree.get_children()
            for element in records:
                tree.delete(element)
            for fila in  Datos.select():
                tree.insert("", 0, text = fila.mi_id, values = (fila.nombre, fila.informacion_general, fila.sodio))
            if len(Datos.select()) == 0:
                raise Exception()
    def buscar(self,var_nombre,tree):
            records = tree.get_children()
            for element in records:
                item=tree.item(element)
                lista=[]
                if item['values'][0]==var_nombre.get():
                    tree.selection_set(element)
                    speech="nombre del producto:" +var_nombre.get()+ " Información general: "+item['values'][1]+ "contenido de sodio: "+item['values'][2]
                    self.engine.say(speech)
                    self.engine.runAndWait()
                    lista.append(element)
                if len(lista)==0:
                    raise Exception()
                    
     
        