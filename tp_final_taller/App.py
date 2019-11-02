from flask import *
import negocio



app = Flask(__name__)


@app.route('/')
def index():
        return render_template('index.html')

@app.route('/menu', methods = ['POST'])
def menu():
    if request.method == 'POST':
        return render_template('menu.html')

@app.route('/menucontrolador', methods = ['POST'])
def menucontrolador():
    if request.method == 'POST':
        if request.form['btnMenu'] == 'Usuarios':
            return redirect('/')
        if request.form['btnMenu'] == 'Vehiculos':
            return redirect('/')
        if request.form['btnMenu'] == 'Clientes':
            return redirect('/')
        if request.form['btnMenu'] == 'HojaDeParte':
            return redirect('/')
        if request.form['btnMenu'] == 'Repuestos':
            return redirect('/')
        if request.form['btnMenu'] == 'Facturacion':

            return redirect('/facturacion')
        if request.form['btnMenu'] == 'Salir':
            return redirect('/')


@app.route('/facturacion')
def facturacion():
    lista=negocio.lista_facturas()
    print(lista)
    return render_template('lista_facturas.html',listafacturas=lista)


@app.route('/add_factura')
def add_factura():
    return 'xd'

@app.route('/update_factura')
def update_factura():
    return 'xd'


if __name__ == '__main__':
    app.run(port = 3000 , debug = True)
