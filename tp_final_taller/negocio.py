from sqlalchemy.orm import sessionmaker
from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
import requests
import json
from datos import *
import datos
from mailjet_rest import Client

import os


Base = declarative_base()
engine = create_engine('mysql://root:852456ale@localhost:3306/python')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()




def dolarPrecioHoy():
 uri_dolar_bcra='https://api.estadisticasbcra.com/usd_of_minorista'
 token_acceso_bcra = 'BEARER eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDQxMTE2NTMsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJhbGVqYW5kcm9kb25ub2xhQGhvdG1haWwuY29tIn0.4UyBkeKkuhRxNbkj2jClwh_9B-AJcYzhCUpwEaHU9ZlXSD0zueup3Y51r19rCVSJX9_jUgHuO06e8yptVHUrgg'
 header = {'Authorization':token_acceso_bcra,'content-type': "application/json"}
 response = requests.get(uri_dolar_bcra,headers = header)
 r_dict = response.json()
 if response.status_code == 200:
  return (r_dict[-1]['v'])
 else:
  return 0
def emitir_mensaje(id_usuario):
    x = buscar_usuario(id_usuario)
    api_key = '08821a1670de40db3d763935decce996'
    api_secret = 'd6a68d8169f451d2403a8b62e33deba8'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": "alejandrodonnola@hotmail.com",
            "Name": "Alejandro"
          },
          "To": [
            {
              "Email": x.email,
              "Name": "Alejandro"
            }
          ],
          "Subject": "Greetings from Mailjet.",
          "TextPart": "My first Mailjet email",
          "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
          "CustomID": "AppGettingStartedTest"
        }
      ]
    }
    result = mailjet.send.create(data=data)
    if result.status_code =='200':
      return result.json()
    else:
      return result.status_code
def buscar_usuario(id_usuario):
    usu = session.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    session.commit()
    if usu is None:
        return False
    else:
        return usu
def buscar_auto(id_patente):
    a = session.query(Auto).filter(Auto.id_patente==id_patente).first()
    session.commit()
    if a is None:
        return False
    else:
        return a
def buscar_auto_cliente(id_usuario):
    a = session.query(Auto).filter(Auto.id_usuario==id_usuario).first()
    session.commit()
    if a is None:
        return False
    else:
        return a
def buscar_repuesto(id_repuesto):
    f = session.query(Repuesto).filter(Repuesto.id_repuesto==id_repuesto).first()
    session.commit()
    if f is None:
        return False
    else:
        return f
def buscar_tipo_repuesto(id_tipoderepuesto):
    f = session.query(Tipo_Repuesto).filter(Tipo_Repuesto.id_tipoderepuesto==id_tipoderepuesto).first()
    session.commit()
    if f is None:
        return False
    else:
        return f
def lista_repuestos_importados(Keyword):
    Keywords = Keyword
    api = finding(appid="Alejandr-TPpython-PRD-0b321054e-314c1a32", config_file=None)
    api_request = { 'keywords': Keywords }
    response = api.execute('findItemsByKeywords', api_request)
    soup = BeautifulSoup(response.content,'lxml')
    totalentries = int(soup.find('totalentries').text)
    items = soup.find_all('item')
    dolarhoy = dolarPrecioHoy()
    cont=0
    lista=[]
    for item in items:
        if cont <= 10:
            cont=cont+1
            cat = item.categoryname.string.lower()
            title = item.title.string.lower()
            price = round(int(round(float(item.currentprice.string)))*dolarhoy)
            url = item.viewitemurl.string.lower()
            lista.append((Keywords,title,price,url,cont))
        else:
            print(lista)
            return lista
            break

def lista_repuestos_nacionales():
        r = session.query(datos.Repuesto).all()
        if(r!=False):
            lista_repuestos=[]
            for f in r:
             x=buscar_tipo_repuesto(f.id_tipo_repuesto)
             lista_repuestos.append((f.id_repuesto,x.descripcion,f.descripcion,f.stock,f.precio_unitario))
            return lista_repuestos
        else:
            return False
def agregar_hoja_de_parte(id_factura,id_mecanico,id_patente,costo_mano_de_obra):
    hoja = HojaDeParte()
    hoja.id_factura=id_factura
    hoja.id_mecanico=id_mecanico
    hoja.id_patente=id_patente
    hoja.costo_mano_de_obra=costo_mano_de_obra
    session.add(hoja)
    session.commit()
    session.refresh(hoja)
    id = hoja.id_hoja
    return id
def agregar_factura(id_usuario):
    fact = Factura()
    fact.id_usuario= id_usuario
    fact.importe_total=0
    fact.fecha_emision=None
    session.add(fact)
    session.commit()
    session.refresh(fact)
    id=fact.id_factura
    return id
def buscar_factura(id_factura):
    f = session.query(Factura).filter(Factura.id_factura==id_factura).first()
    session.commit()
    if f is None:
        return False
    else:
        return f
def actualizar_factura(id_factura,id_usuario,fecha_emision,importe_total):
    f = buscar_factura(id_factura)
    if f is False:
        return False
    else:
        f.fecha_emision = fecha_emision
        f.id_usuario    = id_usuario
        f.importe_total = importe_total
        session.commit()
def actualizar_factura_importe(id_factura,importe_total):
    f = buscar_factura(id_factura)
    if f is False:
        return False
    else:
        f.importe_total = importe_total
        session.commit()
def lista_facturas_usuario(id_usuario):
    u = buscar_usuario(id_usuario)
    if(u!=False):
        facturas  = session.query(Factura).filter(Factura.idUsuario == id_usuario).all()
        lista_facturas=[]
        for f in facturas:
            lista_facturas.append(f)
        return lista_facturas
    else:
        return False
def lista_facturas():
        facturas = session.query(datos.Factura).all()
        if( facturas!=False):
            lista_facturas=[]
            for f in  facturas:
             x=buscar_usuario(f.id_usuario)
             lista_facturas.append((f.id_factura,f.fecha_emision, str(x.nombre)+','+str(x.apellido),x.dni,f.importe_total))
            return lista_facturas
        else:
            return False
def lista_facturas_sin_emitir():
        facturas = session.query(datos.Factura).filter(Factura.fecha_emision == None ).all()
        if(facturas!=False):
            lista_facturas=[]
            for f in facturas:
             x=buscar_usuario(f.id_usuario)
             lista_facturas.append((f.id_factura, str(x.nombre)+','+str(x.apellido),x.dni,f.importe_total))
            return lista_facturas
        else:
            return False
def lista_factura_hojas(id_factura):
        hojas = session.query(datos.HojaDeParte).filter(HojaDeParte.id_factura == id_factura ).all()
        if(hojas!=False):
            lista_hojas=[]
            for h in hojas:
             x=buscar_usuario(h.id_mecanico)
             lista_hojas.append((h.id_hoja, str(x.nombre)+','+str(x.apellido),x.dni,h.id_patente,h.costo_mano_de_obra))
            print(lista_hojas)
            return lista_hojas
        else:
            return False
def agregar_reparacion(idReparacion,patente,idMecanico,fechaIngreso,fechaSalida,estado):
    rep=Reparacion(idReparacion,patente,idMecanico,fechaIngreso,fechaSalida,estado)
    session.add(rep)
    session.commit()
    session.refresh(rep)
    id=rep.idReparacion
    return id
def lista_reparaciones():
        r = session.query(datos.Reparacion).all()
        if( r!=False):
            lista_r=[]
            for f in  r:
             x=buscar_usuario(f.id_mecanico)
             a=buscar_auto(f.id_patente)
             lista_r.append((f.id_reparacion,f.id_patente,str(x.nombre)+','+str(x.apellido),x.dni,f.id_mecanico,f.fecha_ingreso,f.fecha_salida,f.estado_reparacion))
            return lista_r
        else:
            return False
def calcular_importe_factura(id_factura):
    hojas = session.query(datos.HojaDeParte).filter(HojaDeParte.id_factura == id_factura).all()
    importe=0
    for h in hojas:
        importe = importe + h.costo_mano_de_obra
        repuestos=session.query(datos.Hoja_Repuesto).filter(Hoja_Repuesto.id_hoja == h.id_hoja).all()
        for r in repuestos:
            importe = importe + r.precio_total
    actualizar_factura_importe(id_factura,importe)
def buscar_hoja_repuestos(id_hoja):
    repuestos = session.query(datos.Hoja_Repuesto).filter(Hoja_Repuesto.id_hoja == id_hoja).all()
    return repuestos
def buscar_hoja(id_hoja):
    hoja = session.query(datos.HojaDeParte).filter(HojaDeParte.id_hoja == id_hoja).first()
    return hoja
def eliminar_hoja_repuesto(id_hoja,id_repuesto):
    r = session.query(Hoja_Repuesto).filter(Hoja_Repuesto.id_repuesto==id_repuesto and Hoja_Repuesto.id_hoja==id_hoja ).first()
    if r is None:
        return False
    else:
        x=session.delete(r)
        session.commit()
        return True
def agregar_hoja_repuesto(idh,idr,cant):
    hr = Hoja_Repuesto()
    hr.id_hoja=idh
    hr.id_repuesto=idr
    r=buscar_repuesto(idr)
    hr.cantidad=cant
    hr.precio_total=float(cant)*r.precio_unitario
    session.add(hr)
    session.commit()
    session.refresh(hr)

def agregar_repuesto_importado(descripcion,precio_unitario):
    r = Repuesto()
    r.descripcion=descripcion
    r.precio_unitario=precio_unitario
    r.id_tipo_repuesto=2
    r.stock=999
    session.add(r)
    session.commit()
    session.refresh(r)
    id = r.id_repuesto
    return id













