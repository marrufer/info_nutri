"""
El modulo vista.py contiene una clase que se ocupa de todo lo que ve el
usuario en la ventana de la aplicacion.
"""
#Importacion de clases y modulos de tkinter a usar en la vista
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from tkinter import Radiobutton
from tkinter import messagebox
#Importacion de clases propias de la aplicacion
from modelo import Abmc
from registro import RegistroExcepciones

#Clase Vista(), es la clase que incluye la ventana de la aplicacion en tkinter,
#las etiquetas, entradas de datos, botones, treeview, mensajes al usuario.
#Todo lo que el usuario ve.
class Vista():
    def __init__(self,ventana) -> None:
        self.master = ventana
        self.master.title("InfoNutri")
        
        #Declaracion de variables de la aplicación:
        self.var_nombre = StringVar()
        self.var_info_gral = StringVar()
        self.var_sodio = StringVar()
        self.var_nombrem = StringVar()
        self.var_info_gralm = StringVar()
        self.var_sodiom = StringVar()
        
        #Instanciacion de la clase 'Abmc' y 'RegistroExcepciones' para poder usar 
        #los metodos de la clase desde la ventana de la aplicacion:
        self.objeto = Abmc()
        self.registrar = RegistroExcepciones()

        #Etiquetas, nombres de las variables y los formularios como los ve el usuario:
        self.nuevo_producto = Label(self.master,text="Nuevo producto",width=50)
        self.nuevo_producto.grid(row=1,column=0,columnspan=3)
        self.nuevo_producto.configure(background="lightblue")
        self.modificar_producto = Label(self.master,text="Modificar producto",width=50)
        self.modificar_producto.configure(background="lightgreen")
        self.modificar_producto.grid(row=1,column=3,columnspan=3)

        self.nombre = Label(self.master,text="Nombre comercial/\nmarca",width=15,anchor="w")
        self.nombre.grid(row=2,column=0)
        self.info_gral = Label(self.master,text="Información general",width=15,anchor="w")
        self.info_gral.grid(row=4,column=0)
        self.sodio = Label(self.master,text="Sodio",width=15,anchor="w")
        self.sodio.grid(row=5,column=0)

        self.nombrem = Label(self.master,text="Nombre comercial/\nmarca",width=15,anchor="w")
        self.nombrem.grid(row=2,column=3)
        self.infom_gral = Label(self.master,text="Información general",width=15,anchor="w")
        self.infom_gral.grid(row=4,column=3)
        self.sodiom = Label(self.master,text="Sodio",width=15,anchor="w")
        self.sodiom.grid(row=5,column=3)

        #Campos de entrada de datos:
        self.nombre_entry = Entry(self.master,width=30,textvariable=self.var_nombre)
        self.nombre_entry.grid(row=2,column=1,columnspan=2)
        self.info_entry = Entry(self.master,width=30,textvariable=self.var_info_gral)
        self.info_entry.grid(row=4,column=1,columnspan=2)
        self.sodio_contiene = Radiobutton(self.master,
                                        text="Contiene",
                                        variable=self.var_sodio,
                                        value="Contiene",
                                        tristatevalue="x"
                                        )
        self.sodio_contiene.grid(row=5,column=1)
        self.sodio_no_contiene = Radiobutton(self.master,
                                            text="No contiene",
                                            variable=self.var_sodio,
                                            value="No contiene",
                                            tristatevalue="x"
                                            )
        self.sodio_no_contiene.grid(row=5,column=2)

        self.nombrem_entry = Entry(self.master,width=30,textvariable=self.var_nombrem)
        self.nombrem_entry.grid(row=2,column=4,columnspan=2)
        self.infom_entry = Entry(self.master,width=30,textvariable=self.var_info_gralm)
        self.infom_entry.grid(row=4,column=4,columnspan=2)
        self.sodiom_contiene = Radiobutton(self.master,
                                            text="Contiene",
                                            variable=self.var_sodiom,
                                            value="Contiene",
                                            tristatevalue="x"
                                            )
        self.sodiom_contiene.grid(row=5,column=4)
        self.sodiom_no_contiene = Radiobutton(self.master,
                                            text="No contiene",
                                            variable=self.var_sodiom,
                                            value="No contiene",
                                            tristatevalue="x"
                                            )
        self.sodiom_no_contiene.grid(row=5,column=5)

        self.barra = Label(self.master,width=100)
        self.barra.configure(background="lightblue")
        self.barra.grid(row=7,column=0,columnspan=6)
        
        #Declaracion del treeview, con sus 4 columnas:
        self.tree = ttk.Treeview(self.master)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=100, minwidth=70)
        self.tree.column("col2", width=200, minwidth=70)
        self.tree.column("col3", width=100, minwidth=70)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Información general")
        self.tree.heading("col3", text="Sodio")
        self.tree.grid(row=8,rowspan=10, column=1, columnspan=4)

        #Botones de la aplicacion, cada uno apunta a un metodo de la clase Vista()
        #donde se llama a un metodo de Abmc():
        self.guardar = Button(self.master,
                            text="Guardar",width=20, 
                            command=lambda:self.aux_alta()
                            )
        self.guardar.grid(row=6,column=0,columnspan=3)
        self.guardar.configure(background="lightblue")
        self.guardar_modificaciones = Button(self.master,
                                        text="Guardar modificaciones",
                                        width=20,
                                        command=lambda:self.aux_modificar()
                                            )
                                                                    
        self.guardar_modificaciones.configure(background="lightgreen")
        self.guardar_modificaciones.grid(row=6,column=3,columnspan=3)
        self.ver_productos = Button(self.master,
                                    text="Ver productos\nguardados",
                                    width=15,
                                    command=lambda:(self.aux_consulta())
                                    )
        self.ver_productos.grid(row=8,column=0)
        self.ver_productos.configure(background="lightblue")
        self.modificar = Button(self.master,
                                text="Modificar\nproducto",
                                width=15,
                                command=lambda:self.boton_modificar()
                                )
        self.modificar.grid(row=9,column=0)
        self.modificar.configure(background="lightblue")
        self.eliminar_producto = Button(self.master,
                                        text="Eliminar\nproducto",
                                        width=15,
                                        command=lambda:self.aux_baja()
                                        )
        self.eliminar_producto.grid(row=10,column=0)
        self.eliminar_producto.configure(background="lightblue")
        self.salir = Button(self.master,
                            text="Salir",
                            command=self.master.quit,
                            width=10
                            )
        self.salir.grid(row=23,column=5,columnspan=2)
        self.salir.configure(background="lightblue")
    
    #Mensajes al usuario:
    def aux_alta(self):
        try:
            self.objeto.alta(self.tree,self.var_nombre,self.var_info_gral,self.var_sodio)
            self.var_nombre.set("")
            self.var_info_gral.set("")
            self.sodio_contiene.deselect()
            self.sodio_no_contiene.deselect()
        except Exception:
            self.registrar.registrar_error(135,"vista.py")
            messagebox.showerror("Error",
                                "El nombre solo puede contener letras y/o números.\
                                \nDebe completar todos los campos del formulario"
                                )
    def aux_consulta(self):
        try:
            self.objeto.consulta(self.tree)
        except:
            messagebox.showerror("InfoNutri",
                                "Todavía no hay productos guardados"
                                )
    def aux_baja(self):
        valor = self.tree.selection()
        if valor:
            if messagebox.askokcancel("InfoNutri",
                                    "Está a punto de eliminar un producto.\
                                    \nPresione Aceptar para continuar"
                                    ):
                self.objeto.baja(self.tree,valor)
                messagebox.showinfo("InfoNutri",
                                    "Producto eliminado"
                                    )
            else:
                self.tree.selection_remove(self.tree.selection())
        else:
            messagebox.showerror("Error",
                                "Debe seleccionar un producto de la lista para eliminar"
                                )
    def aux_modificar(self):
        valor = self.tree.selection()
        if valor:
            try:            
                self.objeto.modificar(self.tree,self.var_nombrem,self.var_info_gralm,self.var_sodiom)
                self.var_nombrem.set("")
                self.var_info_gralm.set("")
                self.sodiom_contiene.deselect()
                self.sodiom_no_contiene.deselect()  
                messagebox.showinfo("InfoNutri",
                                    "Modificaciones guardadas correctamente"
                                    )
            except Exception:
                self.registrar.registrar_error(180,"vista.py")
                messagebox.showerror("Error", 
                                    "Debe completar todos los campos."
                                    ) 
        else:
            messagebox.showerror("Error",
                                "Seleccione un producto para modificarlo"
                                )
    #boton_modificar, se utiliza para visualizar los datos del 
    #producto seleccionado para ser modificado en el formulario 'Modificar producto'
    def boton_modificar(self):
        try:
            valor = self.tree.selection()
            item = self.tree.item(valor)
            self.var_nombrem.set(item['values'][0])
            self.var_info_gralm.set(item['values'][1])
            self.var_sodiom.set(item['values'][2])
        except (IndexError):
            messagebox.showerror("Modificación de producto",
                                "Seleccione un producto de la lista para modificar"
                                )      
    




