from flask import *
import negocio
from datetime import date



app = Flask(__name__)


@app.route('/')
def index():
        return render_template('index.html')

@app.route('/menu', methods = ['POST'])
def menu():
    if request.method == 'POST':
        return render_template('menu.html')

@app.route('/facturacion')
def facturacion():
    return render_template('lista_facturas.html',listafacturas=negocio.lista_facturas())

@app.route('/menucontroladorLF', methods = ['POST'])
def menucontroladorLF():
 if request.method == 'POST':
    if request.form['btnMenuLF'] == 'Volver':
        return redirect('/menu',code=307)
    if request.form['btnMenuLF'] == 'Emitir':
        return redirect('/facturacion/facturasinemitir',code=307)


@app.route('/facturacion/facturahojas/<string:id>')
def facturahojas(id):
        return render_template('lista_factura_hojas.html',listafacturas=negocio.lista_factura_hojas(int(id)))

@app.route('/facturacion/facturasinemitir',methods = ['POST'])
def facturasinemitir():
      if request.method == 'POST':
        return render_template('lista_facturas_sinemitir.html',listafacturas=negocio.lista_facturas_sin_emitir())

@app.route('/facturacion/emitir/<string:id>')
def emitir(id):
        f=negocio.buscar_factura(id)

        u=negocio.buscar_usuario(f.id_usuario)
        today = date.today()
        return render_template('form_emitirfactura.html',id_factura=id,usuario_dni=u.dni
                               ,usuario_nombre=u.nombre,usuario_apellido=u.apellido
                               ,fecha=today.strftime("%Y-%m-%d"))

@app.route('/controladoremision', methods = ['POST'] )
def controladoremision():
    if request.method == 'POST':
        id_factura = request.form["btnEmitir"]
        today = date.today()
        fecha=today.strftime("%Y-%m-%d")
        f=negocio.buscar_factura(id_factura)
        negocio.emitir_mensaje(f.id_usuario)
        negocio.actualizar_factura(f.id_factura,f.id_usuario,fecha,f.importe_total)
        return redirect("/facturacion")





@app.route('/add_factura')
def add_factura():
    return 'xd'

@app.route('/update_factura')
def update_factura():
    return 'xd'

@app.route('/repuestos')
def repuestos():
    return render_template('lista_repuestos.html',listafacturas=negocio.lista_facturas())

if __name__ == '__main__':
    app.run(port = 3000 , debug = True)
