from peewee import *

base = SqliteDatabase("informacion_nutricional.db")
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
 


