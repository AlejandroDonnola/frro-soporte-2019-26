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
    if request.form['btnMenuLF'] == 'Agregar':
        return redirect('/factura',code=307)
    if request.form['btnMenuLF'] == 'Emitir':
        return redirect('/facturacion/facturasinemitir',code=307)


@app.route('/facturacion/facturahojas/<string:id>')
def facturahojas(id):
        return render_template('lista_factura_hojas.html',listahojas=negocio.lista_factura_hojas(int(id)),id_factura=id)

@app.route('/hojas',methods = ['POST'])
def controladorfactuahojas():
     if request.method == 'POST':
         id_factura=request.form['btnAgregar']
         f=negocio.buscar_factura(id_factura)
         a=negocio.buscar_auto_cliente(f.id_usuario)
         return render_template('form_hoja.html',id_factura=id_factura,id_cliente=f.id_usuario,id_patente=a.id_patente)


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
                               ,fecha=today.strftime("%Y-%m-%d"),importe=f.importe_total)

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

@app.route('/factura', methods = ['POST'] )
def factura():
    return render_template("form_factura.html",listaclientes=negocio.lista_clientes())

@app.route('/controladorfactura', methods = ['POST'] )
def controladorfactura():
    if request.method == 'POST':
        if request.form["id_cliente"] != None:
             negocio.agregar_factura(request.form["id_cliente"])
             return redirect('/facturacion')


@app.route('/add_factura')
def add_factura():
    return 'xd'

@app.route('/update_factura')
def update_factura():
    return 'xd'

@app.route('/repuestos')
def repuestos():
    return render_template('lista_repuestos_nacionales.html',listarepuestos=negocio.lista_repuestos_nacionales())

@app.route('/repuestoscategoriaimportado', methods = ['POST'])
def repuestoscategoriaimportado():
    if request.method == 'POST':
     if request.form['Categorias'] == '1':
        return render_template('lista_repuestos_importado.html',listarepuestos=negocio.lista_repuestos_importados("Wheels"))
     if request.form['Categorias'] == '2':
        return render_template('lista_repuestos_importado.html',listarepuestos=negocio.lista_repuestos_importados("steering wheel"))
     if request.form['Categorias'] != '1' or request.form['Categorias']!='2':
        return render_template('lista_repuestos_importado.html')

@app.route('/repuestos/importados')
def repuestos_importados():
    return render_template('lista_repuestos_importado.html')

@app.route('/repuestos/importados/llantas')
def repuestos_importados_llantas():
    return render_template('lista_repuestos_importado.html',listarepuestos=negocio.lista_repuestos_importados())

@app.route('/repuestos/importados/volantes')
def repuestos_importados_volantes():
    return render_template('lista_repuestos_importado.html',listarepuestos=negocio.lista_repuestos_importados())

@app.route('/controladorhojas', methods = ['POST'])
def controladorhojas():
    if request.method == 'POST':
     id_mecanico = request.form['id_mecanico']
     id_patente = request.form['id_patente']
     id_factura = request.form['id_factura']
     costo_mano_de_obra = request.form['costo_mano_de_obra']
     u= '/facturacion/facturahojas/'+request.form['id_factura']
     negocio.agregar_hoja_de_parte(id_factura,id_mecanico,id_patente,costo_mano_de_obra)
     negocio.calcular_importe_factura(int(id_factura))
    return redirect(u)



@app.route('/hoja/<string:id>/repuestos')
def hojarepuestos(id):
    r=negocio.buscar_hoja_repuestos(int(id))
    id_factura=negocio.buscar_hoja(int(id)).id_factura
    repuestos=[]
    for re in r:
        x=negocio.buscar_repuesto(re.id_repuesto)
        repuestos.append((x.id_repuesto,x.id_tipo_repuesto,x.descripcion,x.stock,x.punto_pedido,x.precio_unitario))
    print(repuestos)
    return render_template('lista_hoja_repuestos.html',repuestos= repuestos,id_hoja=id,id_factura=id_factura)

@app.route('/hoja/<string:id>/repuestos/eliminar/<string:idr>')
def eliminar_hoja_repuesto(id,idr):
    negocio.eliminar_hoja_repuesto(id,idr)
    negocio.calcular_importe_factura(negocio.buscar_hoja(int(id)).id_factura)
    return redirect('/hoja/'+id+'/repuestos')

@app.route('/hoja/<string:id>/repuestos/agregar', methods=['POST'])
def agregarrepuesto(id):
     if request.method == 'POST':
      return render_template('form_repuesto.html',repuestos=negocio.lista_repuestos_importados("wheels"),id_hoja=request.form['btnAgregar'])

@app.route('/controladorrepuesto', methods=['POST'])
def controladorrepuesto():
    if request.method == 'POST':
        cantidad=request.form['cantidad']
        id_hoja=request.form['id_hoja']
        select=request.form['Repuestos']
        r = negocio.lista_repuestos_importados("wheels")
        descripcion=r[int(select)][1]
        idr=negocio.agregar_repuesto_importado(descripcion[:10],r[int(select)][2])
        negocio.agregar_hoja_repuesto(id_hoja,idr,cantidad)
        negocio.calcular_importe_factura(negocio.buscar_hoja(int(id_hoja)).id_factura)
        return redirect('/hoja/'+id_hoja+'/repuestos')



if __name__ == '__main__':
    app.run(port = 3000 , debug = True)
