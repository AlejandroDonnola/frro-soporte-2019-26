## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .

from tkinter import Tk, Entry, Button, StringVar, font

root = Tk()
root.geometry('250x175')
root.title("Calculadora")
datosEntrada=StringVar()
datos=""
fuente=font.Font(weight="bold")
entrada = Entry(root, textvariable=datosEntrada, font=fuente, width=18)
entrada.grid(columnspan=4, padx=10, pady=10)


def press(boton):
    global datos
    if boton=='=':
        try:
            total = str(eval(datos))
            print("Resultado= "+total)
            datos = ""
        except ZeroDivisionError:
            print("NO SE PUEDE DIVIDIR POR CERO!!")
            datos=""
        except:
            print("Error")
            datos = ""
    else:
        datos= datos+str(boton)
        datosEntrada.set(datos)


boton1 = Button(root, text='1', command=lambda: press(1), height=1, width=4)
boton2 = Button(root, text='2', command=lambda: press(2), height=1, width=4)
boton3 = Button(root, text='3', command=lambda: press(3), height=1, width=4)
boton4 = Button(root, text='4', command=lambda: press(4), height=1, width=4)
boton5 = Button(root, text='5', command=lambda: press(5), height=1, width=4)
boton6 = Button(root, text='6', command=lambda: press(6), height=1, width=4)
boton7 = Button(root, text='7', command=lambda: press(7), height=1, width=4)
boton8 = Button(root, text='8', command=lambda: press(8), height=1, width=4)
boton9 = Button(root, text='9', command=lambda: press(9), height=1, width=4)
boton0 = Button(root, text='0', command=lambda: press(0), height=1, width=4)
btnSuma = Button(root, text='+', command=lambda: press('+'), height=1, width=4)
btnMenos = Button(root, text='-', command=lambda: press('-'), height=1, width=4)
btnProducto = Button(root, text='*', command=lambda: press('*'), height=1, width=4)
btnCociente = Button(root, text='/', command=lambda: press('/'), height=1, width=4)
btnIgual = Button(root, text='=', command=lambda: press('='), height=1, width=11)
boton7.grid(row=2, column=0, padx=(0, 1), pady=(3, 3))
boton8.grid(row=2, column=1, padx=(0, 1), pady=(3, 3))
boton9.grid(row=2, column=2, padx=(0, 1), pady=(3, 3))
btnSuma.grid(row=2, column=3, padx=(0, 1), pady=(3, 3))
boton4.grid(row=6, column=0, padx=(0, 1), pady=(3, 3))
boton5.grid(row=6, column=1, padx=(0, 1), pady=(3, 3))
boton6.grid(row=6, column=2, padx=(0, 1), pady=(3, 3))
btnMenos.grid(row=6, column=3, padx=(0, 1), pady=(3, 3))
boton1.grid(row=10, column=0, padx=(0, 1), pady=(3, 3))
boton2.grid(row=10, column=1, padx=(0, 1), pady=(3, 3))
boton3.grid(row=10, column=2, padx=(0, 1), pady=(3, 3))
btnCociente.grid(row=10, column=3, padx=(0, 1), pady=(3, 3))
boton0.grid(row=14, column=0, padx=(0, 1), pady=(3, 3))
btnIgual.grid(row=14, column=1, columnspan=2, padx=(0, 1), pady=(3, 3))
btnProducto.grid(row=14, column=3, padx=(0, 1), pady=(3, 3))
root.mainloop()
