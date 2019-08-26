from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio

import tkinter as tk
from tkinter import ttk, Entry, IntVar, StringVar, Label, Frame, Button


class Interfaz(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(root)
        self.ventana = ventana
        self.ventana.title("ABM Socios")
        self.ventana.geometry('825x285+600+200')
        self.ventana.resizable(0, 0)

        self.formulario = ttk.Treeview(self.ventana, columns=("nombre", "apellido", "dni"), selectmode=tk.BROWSE)
        self.formulario.heading("#0", text="Id")
        self.formulario.heading("nombre", text="Nombre")
        self.formulario.heading("apellido", text="Apellido")
        self.formulario.heading("dni", text="DNI")
        self.formulario.place(x=10, y=10)

        self.marco = Frame(self.ventana)
        self.marco.place(y=240, x=10, width=801)

        self.btnAlta = Button(self.marco, text="Alta", width=6, command=alta)
        self.btnAlta.grid(row=0, column=0)
        self.btnBaja = Button(self.marco, text="Baja", width=6, command=baja)
        self.btnBaja.grid(row=0, column=1, padx=3)
        self.btnModificar = Button(self.marco, text="Modificación", width=12, command=modificacion)
        self.btnModificar.grid(row=0, column=2)

        self.mostrar_todos()

    def mostrar_todos(self):
        records = self.formulario.get_children()
        for element in records:
            self.formulario.delete(element)
        socios= NegocioSocio().todos()
        for socio in socios:
            self.formulario.insert("", tk.END, text=socio.IdSocio, values=(socio.Nombre, socio.Apellido, socio.DNI))

def alta():
    nombre = StringVar()
    apellido = StringVar()
    dni = IntVar()
    alta_window = tk.Toplevel(root)
    alta_window.title("Alta")
    alta_window.geometry('230x120+625+400')
    alta_window.resizable(0, 0)

    label = Label(alta_window, text="Nombre")
    label.grid(row=0, column=0, padx=20)
    entryNomb = Entry(alta_window, textvariable=nombre, width=20)
    entryNomb.grid(row=0, column=1, pady=5)

    label = Label(alta_window, text="Apellido")
    label.grid(row=1, column=0, padx=20)
    entryApel = Entry(alta_window, textvariable=apellido, width=20)
    entryApel.grid(row=1, column=1)

    label = Label(alta_window, text="DNI")
    label.grid(row=2, column=0, padx=20)
    entryDNI = Entry(alta_window, textvariable=dni, width=20)
    entryDNI.grid(row=2, column=1, pady=5)

    btnAceptar = Button(alta_window, text='Aceptar', command=lambda: agregar(nombre, apellido, dni))
    btnAceptar.grid(row=3, column=0, padx=10, pady=5)
    btnCancelar = Button(alta_window, text='Cancelar', command=alta_window.destroy)
    btnCancelar.grid(row=3, column=1, padx=10, pady=5)

    def agregar(nombre, apellido, dni):
        if (nombre.get() != "") and (apellido.get() != "") and (dni.get() != ""):
            socio = Socio(Nombre=nombre.get(), Apellido=apellido.get(), DNI=dni.get())
            NegocioSocio().alta(socio)
            app.mostrar_todos()
            alta_window.destroy()

def baja():
    seleccion = app.formulario.selection()
    id_socio = app.formulario.item(seleccion, option="text")
    if id_socio != "":
        baja_window = tk.Toplevel(root)
        baja_window.title("Baja")
        baja_window.geometry('195x65+625+400')
        baja_window.resizable(0, 0)
        label = Label(baja_window, text="¿Desea dar de baja al socio?")
        label.grid(row=0, columnspan=2, padx=20, pady=(5, 0))
        btnAceptar = Button(baja_window, text='Aceptar', command=lambda: borrar(id_socio))
        btnAceptar.grid(row=5, column=0, padx=10, pady=5)
        btnCancelar = Button(baja_window, text='Cancelar', command=baja_window.destroy)
        btnCancelar.grid(row=5, column=1, padx=10, pady=5)

    def borrar(id_socio):
        NegocioSocio().baja(id_socio)
        app.mostrar_todos()
        baja_window.destroy()

def modificacion():
    seleccion = app.formulario.selection()
    id_socio= app.formulario.item(seleccion, option="text")
    if id_socio !="":
        modifica_window = tk.Toplevel(root)
        modifica_window.title("Modificación")
        modifica_window.geometry('235x150+625+400')
        modifica_window.resizable(0, 0)
        nombre = StringVar()
        apellido = StringVar()
        dni = IntVar()

        label = Label(modifica_window, text="Id: ")
        label.grid(row=0, column=0, padx=20)
        label = Label(modifica_window, text=str(id_socio))
        label.grid(row=0, column=1, padx=20)

        label = Label(modifica_window, text="Nombre")
        label.grid(row=1, column=0, padx=20)
        entryNomb = Entry(modifica_window, textvariable=nombre, width=20)
        entryNomb.grid(row=1, column=1)

        label = Label(modifica_window, text="Apellido")
        label.grid(row=2, column=0, padx=20)
        entryApel = Entry(modifica_window, textvariable=apellido, width=20)
        entryApel.grid(row=2, column=1, pady=5)

        label = Label(modifica_window, text="Dni")
        label.grid(row=3, column=0, padx=20)
        entryDNI = Entry(modifica_window, textvariable=dni, width=20)
        entryDNI.grid(row=3, column=1)

        btnAceptar = Button(modifica_window, text='Aceptar', command=lambda: modificar(id_socio, nombre, apellido, dni))
        btnAceptar.grid(row=4, column=0, padx=10, pady=5)
        btnCancelar = Button(modifica_window, text='Cancelar', command=modifica_window.destroy)
        btnCancelar.grid(row=4, column=1, padx=10, pady=5)

    def modificar(id_socio, nombre, apellido, dni):
        if (nombre.get() != "") and (apellido.get() != "") and (dni.get() != ""):
            socio= Socio(IdSocio=id_socio, Nombre=nombre.get(), Apellido=apellido.get(), DNI=dni.get())
            NegocioSocio().modificacion(socio)
            app.mostrar_todos()
            modifica_window.destroy()


root = tk.Tk()
app = Interfaz(root)
root.mainloop()
