## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 

import tkinter as tk
from tkinter import ttk


class Application(ttk.Frame):
    def __init__(self, main_window, resolucion):
        super().__init__(main_window)
        main_window.title("Ciudades de Argentina")
        main_window.geometry(resolucion)
        self.treeview = ttk.Treeview(self, columns="cod_postal", selectmode=tk.BROWSE)
        self.treeview.heading("#0", text="Ciudad")
        self.treeview.heading("cod_postal", text="Código Postal")
        self.treeview.insert("", tk.END, text="Rosario", values="2000")
        self.treeview.insert("", tk.END, text="La Plata", values="1900")
        self.treeview.insert("", tk.END, text="Mendoza", values="5500")
        self.treeview.insert("", tk.END, text="Capitán Bermudez", values="2154")
        self.treeview.insert("", tk.END, text="Santa Fe", values="3000")
        self.treeview.grid(row=0)
        self.grid()


if __name__=='__main__':
    main_window = tk.Tk()
    res = '400x230+600+200'
    app = Application(main_window, res)
    app.mainloop()
