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


def listarRepuestos(Keyword):
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
        if cont != 20:
            cont=cont+1
            cat = item.categoryname.string.lower()
            title = item.title.string.lower()
            price = int(round(float(item.currentprice.string)))*dolarhoy
            url = item.viewitemurl.string.lower()
            lista.append(item)
        else:
            return lista
            break


    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + str(price) + '\n')
    print('url:\n' + url + '\n')
    input(items[1])





def agregar_rol(codRol,descripcion,usuarios):
    rol = Rol(codRol,descripcion,usuarios)
    session.add(rol)
    session.commit()
    session.refresh(rol)
    id=rol.codRol
    return id


def agregar_usuario(idUsuario,nombre,apellido,dni,email,password,tel,codRol,habilitado,autos,reparaciones,hojas):
    usu=Usuario(idUsuario,nombre,apellido,dni,email,password,tel,codRol,habilitado,autos,reparaciones,hojas)
    session.add(usu)
    session.commit()
    session.refresh(usu)
    id=usu.dni
    return id

def buscar_usuario(id_usuario):
    usu = session.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    session.commit()
    if usu is None:
        return False
    else:
        return usu

def agregar_auto():

    return 0

def agregar_repuesto():

    return id

def agregar_hoja_de_parte(idHoja,idMecanico,patente,costo_manodeObra,idRepuesto,cantidad):
    hoja = HojaDeParte(idHoja,idMecanico,patente,costo_manodeObra,idRepuesto,cantidad)
    session.add(hoja)
    session.commit()
    session.refresh(hoja)
    id = hoja.idHoja
    return id

def agregar_factura(id_factura,fecha_emision,id_hoja,importe_total):
    fact = Factura(id_factura,fecha_emision,id_hoja,importe_total)
    session.add(fact)
    session.commit()
    session.refresh(fact)
    id=fact.id_factura
    return id

def borrar_factura(idFactura):
    f = session.query(Factura).filter(Factura.idFactura==idFactura).first()
    if f is None:
        return False
    else:
        x=session.delete(f)
        session.commit()
        return True

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

def lista_facturas_usuario(id_usuario):
    u = buscar_usuario(id_usuario)
    if(u!=False):
        facturas      = session.query(Factura).filter(Factura.idUsuario == id_usuario).all()
        lista_facturas=[]
        for f in facturas:
            lista_facturas.append(f)
        return lista_facturas
    else:
        return False

def lista_facturas():
        facturas = session.query(datos.Factura).all()
        if(facturas!=False):
            lista_facturas=[]
            for f in facturas:
             x=buscar_usuario(f.id_usuario)
             lista_facturas.append((f.id_factura,f.fecha_emision, str(x.nombre)+','+str(x.apellido),x.dni,f.importe_total))
            print(lista_facturas)
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



def agregar_reparacion(idReparacion,patente,idMecanico,fechaIngreso,fechaSalida,estado):
    rep=Reparacion(idReparacion,patente,idMecanico,fechaIngreso,fechaSalida,estado)
    session.add(rep)
    session.commit()
    session.refresh(rep)
    id=rep.idReparacion
    return id

def agregar_proveedor():

    return 0
def agregar_proveedor_repuesto():

    return 0



