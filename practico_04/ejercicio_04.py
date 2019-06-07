## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra .

import tkinter as tk
from tkinter import font
from practico_04.ejercicio_03 import Application


class CreaMarco(tk.Frame):
    def __init__(self, padre=None):     
        super().__init__(padre)
        self.padre = padre
        self.grid(row=1)
        self.crear_controles()

    def crear_controles(self):          

        def agregar_ciudad():
            self.lbl['text'] = ""
            ciudad = tk.StringVar()
            cp = tk.StringVar()
            alt_window = tk.Toplevel(root)
            alt_window.title("Agregar nueva ciudad")
            alt_window.geometry('345x170+625+400')
            alt_window.resizable(0, 0)
            lblCiudad = tk.Label(alt_window, text="Nombre de la ciudad")
            lblCiudad.grid(row=0, columnspan=2, padx=20, pady=(5, 0))
            entryCiudad = tk.Entry(alt_window, textvariable=ciudad, width=50)
            entryCiudad.grid(row=1, columnspan=2, padx=20, pady=(0, 5))
            lblCP = tk.Label(alt_window, text="Código Postal")
            lblCP.grid(row=2, columnspan=2, padx=20, pady=(5, 0))
            entryCP = tk.Entry(alt_window, textvariable=cp, width=50)
            entryCP.grid(row=3, columnspan=2, padx=20, pady=(0, 5))
            lbl = tk.Label(alt_window, text="")
            lbl.grid(row=4, columnspan=2, padx=20, pady=5)

            def agregar(ciudad, cp):
                if ciudad.get() != "" and cp.get() != "":
                    app.treeview.insert("", tk.END, text=ciudad.get(), values=cp.get())
                    app.treeview.grid()
                    alt_window.destroy()
                else:
                    lbl = tk.Label(alt_window, text="Primero ingrese la ciudad con su Código Postal.", font=font.Font(size=10, weight="bold"))
                    lbl.grid(row=4, columnspan=3, padx=10, pady=5)

            btnAceptar = tk.Button(alt_window, text='Aceptar', command=lambda: agregar(ciudad, cp))
            btnAceptar.grid(row=5, column=0, padx=10, pady=5)
            btnCancelar = tk.Button(alt_window, text='Cancelar', command=alt_window.destroy)
            btnCancelar.grid(row=5, column=1, padx=10, pady=5)

        self.btnAlta = tk.Button(self, text='Agregar ciudad...', command=agregar_ciudad)

        def borrar_ciudad():
            seleccion = app.treeview.selection()
            nombre = app.treeview.item(seleccion, option="text")
            codigo = app.treeview.item(seleccion, 'values')
            if nombre != '' and codigo != '':
                self.lbl['text'] = ""
                alt_window = tk.Toplevel(root)
                alt_window.title("Borrar ciudad")
                alt_window.geometry('250x80+625+400')
                alt_window.resizable(0, 0)
                lblCiudad = tk.Label(alt_window, text="¿Desea borrar la ciudad de "+nombre+"?")
                lblCiudad.grid(row=0, columnspan=2, padx=20, pady=(5, 0))

                def borrar(ciudad):
                    app.treeview.delete(ciudad)
                    app.treeview.grid()
                    alt_window.destroy()

                btnAceptar = tk.Button(alt_window, text='Aceptar', command=lambda: borrar(seleccion))
                btnAceptar.grid(row=5, column=0, padx=10, pady=5)
                btnCancelar = tk.Button(alt_window, text='Cancelar', command=alt_window.destroy)
                btnCancelar.grid(row=5, column=1, padx=10, pady=5)
            else:
                self.lbl['text'] = "Selecciona una ciudad"

        self.btnBaja = tk.Button(self, text='Borrar ciudad', command=borrar_ciudad)

        def modificar_ciudad():
            seleccion = app.treeview.selection()
            nombre = app.treeview.item(seleccion, option="text")
            codigo = app.treeview.item(seleccion, 'values')
            if nombre != '' and codigo != '':
                self.lbl['text'] = ""
                ciudad = tk.StringVar()
                cp = tk.StringVar()
                alt_window = tk.Toplevel(root)
                alt_window.title("Modificar ciudad")
                alt_window.geometry('345x170+625+400')
                alt_window.resizable(0, 0)
                lblCiudad = tk.Label(alt_window, text="Nombre de la ciudad")
                lblCiudad.grid(row=0, columnspan=2, padx=20, pady=(5, 0))
                entryCiudad = tk.Entry(alt_window, textvariable=ciudad, width=50)
                entryCiudad.grid(row=1, columnspan=2, padx=20, pady=(0, 5))
                lblCP = tk.Label(alt_window, text="Código Postal")
                lblCP.grid(row=2, columnspan=2, padx=20, pady=(5, 0))
                entryCP = tk.Entry(alt_window, textvariable=cp, width=50)
                entryCP.grid(row=3, columnspan=2, padx=20, pady=(0, 5))
                lbl = tk.Label(alt_window, text="")
                lbl.grid(row=4, columnspan=2, padx=20, pady=5)

                def modificar(elemento, ciudad, cp):
                    if ciudad.get() != "" and cp.get() != "":
                        app.treeview.item(elemento, text=ciudad.get(), values=cp.get())
                        app.treeview.grid()
                        alt_window.destroy()
                    else:
                        lbl = tk.Label(alt_window, text="Primero ingrese la ciudad con su Código Postal.", font=font.Font(size=10, weight="bold"))
                        lbl.grid(row=4, columnspan=2, padx=10, pady=5)

                btnAceptar = tk.Button(alt_window, text='Aceptar', command=lambda: modificar(seleccion, ciudad, cp))
                btnAceptar.grid(row=5, column=0, padx=10, pady=5)
                btnCancelar = tk.Button(alt_window, text='Cancelar', command=alt_window.destroy)
                btnCancelar.grid(row=5, column=1, padx=10, pady=5)
            else:
                self.lbl['text'] = "Selecciona una ciudad"

        self.btnModifica = tk.Button(self, text='Modificar ciudad', command=modificar_ciudad)
        self.btnSalir = tk.Button(self, text="Salir", width=10, command=self.padre.destroy)  
        self.lbl = tk.Label(self, text="", font=font.Font(size=10, weight="bold"))
        self.lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
        self.btnModifica.grid(row=1, column=1, padx=10, pady=5)
        self.btnSalir.grid(row=2, column=1)
        self.btnAlta.grid(row=1, column=0, padx=10, pady=5)
        self.btnModifica.grid(row=1, column=1, padx=10, pady=5)
        self.btnBaja.grid(row=1, column=2, padx=10, pady=5)
        self.btnSalir.grid(row=2, column=1, pady=5)


root = tk.Tk()
res = '400x330+600+200'
app = Application(root, res)
CreaMarco(padre=root)
root.mainloop()
