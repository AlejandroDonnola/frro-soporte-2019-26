## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 

from tkinter import Tk, IntVar, Label, Entry, Button

root = Tk()
root.geometry('335x80')
root.title("Calculadora")
valor1 = IntVar()
valor2 = IntVar()
labelValor1 = Label(root, text="Primer operando")
entryValor1 = Entry(root, textvariable=valor1, width=10)
labelValor1.grid(row=0, column=0, padx=(20, 10), pady=(10, 2))
entryValor1.grid(row=1, column=0, padx=(40, 30), pady=(2, 10))
labelValor2 = Label(root, text="Segundo operando")
entryValor2 = Entry(root, textvariable=valor2, width=10)
labelValor2.grid(row=0, column=1, padx=(10, 5), pady=(10, 2))
entryValor2.grid(row=1, column=1, padx=(20, 10), pady=(2, 10))


def operacion(operador):
    if operador=='+':
        print("Resultado= "+str(valor1.get() + valor2.get()))
    elif operador=='-':
        print("Resultado= "+str(valor1.get() - valor2.get()))
    elif operador=='*':
        print("Resultado= "+str(valor1.get() * valor2.get()))
    else:
        try:
            res=(valor1.get() / valor2.get())
        except ZeroDivisionError:
            print("NO SE PUEDE DIVIDIR POR CERO!")
        else:
            print("Resultado= "+str(res))


buttonOperador = Button(root, text="+", command=lambda: operacion('+'))
buttonOperador.grid(row=1, column=2, padx=(0, 0), pady=(2, 2))
buttonOperador = Button(root, text="-", command=lambda: operacion('-'))
buttonOperador.grid(row=1, column=3, padx=(0, 1), pady=(2, 2))
buttonOperador = Button(root, text="*", command=lambda: operacion('*'))
buttonOperador.grid(row=1, column=4, padx=(0, 1), pady=(2, 2))
buttonOperador = Button(root, text="/", command=lambda: operacion('/'))
buttonOperador.grid(row=1, column=5, padx=(0, 3), pady=(2, 2))
root.mainloop()
