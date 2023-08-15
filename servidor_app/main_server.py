from tkinter import Tk
from vista_server import Vista

class Controller:
   
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = Vista(self.root_controler)

if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)
    root_tk.mainloop()