from tkinter import StringVar
from tkinter import messagebox
from tkinter import Entry
from tkinter import Label
from tkinter import Button

from tkinter import ttk

import os
import sys
# ===========================================================
from pathlib import Path

import subprocess
import threading
from modelo_server import Ac


theproc=""

class Vista:
    def __init__(self, window):
        self.root = window
        self.root.title("Servidor InfoNutri")
        self.objeto=Ac()
        self.var_nombre=StringVar()
        self.var_info_gral=StringVar()
        self.var_sodio=StringVar()
        
        self.raiz = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.raiz, 'udp_server.py')
    
        self.titulo = Label(self.root, text="Servidor", bg="DarkOrchid3", fg="thistle1", height=1, width=70)
        self.titulo.grid(row=0, column=0, columnspan=5, padx=1, pady=1)



        self.boton_prender=Button(self.root, text="Prender", command=lambda:self.try_connection())
        self.boton_prender.grid(row=6, column=1)

        self.boton_apagar=Button(self.root, text="Apagar", command=lambda:self.stop_server())
        self.boton_apagar.grid(row=6, column=3)
        self.titulo = Label(self.root, text="Informacion nutricional", bg="DarkOrchid3", fg="thistle1", height=1, width=70)
        self.titulo.grid(row=7, column=0, columnspan=5, padx=1, pady=1)
        
        self.boton_ver_productos=Button(self.root,text="Ver productos",command=lambda:self.objeto.consulta(self.tree))
        self.boton_ver_productos.grid(row=8,column=1)
        
        self.buscar=Label(self.root,text="Nombre producto")
        self.buscar.grid(row=8,column=2)
        self.nombre=Entry(self.root,width=30,textvariable=self.var_nombre)
        self.nombre.grid(row=8,column=3)
        self.boton_buscar=Button(self.root,text="Buscar producto",command=lambda:self.aux_buscar())
        self.boton_buscar.grid(row=8,column=4)
        
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=100, minwidth=70)
        self.tree.column("col2", width=200, minwidth=70)
        self.tree.column("col3", width=100, minwidth=70)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Información general")
        self.tree.heading("col3", text="Sodio")
        self.tree.grid(row=9,rowspan=10, column=1, columnspan=4)
        
        print("prender")
    def aux_buscar(self):
        try:
            self.objeto.buscar(self.var_nombre,self.tree)
        except:
            messagebox.showerror("InfoNutri",
                                "No encontramos ese producto")
    def try_connection(self, ): 

        if theproc != "":
            theproc.kill()
            threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
        else:
            threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
        
    def lanzar_servidor(self, var):

        the_path =  self.ruta_server
        if var==True:
            global theproc
            theproc = subprocess.Popen([sys.executable, the_path])
            theproc.communicate()

        else:
            print("")

    # =================== INNIT AND STOP SERVER ====================== 
    def stop_server(self, ):

        global theproc
        if theproc !="":
            theproc.kill() 
