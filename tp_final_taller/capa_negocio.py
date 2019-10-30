from sqlalchemy.orm import sessionmaker
from datos import *

Base = declarative_base()
engine = create_engine('mysql://root:852456ale@localhost:3306/python')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


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
    usu = session.query(Usuario).filter(Usuario.idUsuario == id_usuario).first()
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

def agregar_factura(idFactura,fechaEmision,idHoja,importeTotal):
    fact = Factura(idFactura,fechaEmision,idHoja,importeTotal)
    session.add(fact)
    session.commit()
    session.refresh(fact)
    id=fact.idFactura
    return id

def borrar_factura(idFactura):
    f = session.query(Factura).filter(Factura.idFactura==idFactura).first()
    if f is None:
        return False
    else:
        x=session.delete(f)
        session.commit()
        return True

def buscar_factura(idFactura):
    f = session.query(Factura).filter(Factura.idFactura==idFactura).first()
    session.commit()
    if f is None:
        return False
    else:
        return f

def actualizar_factura(idFactura,fechaEmision,idHoja,importeTotal):
    f = buscar_factura(idFactura)
    if f is False:
        return False
    else:
        f.fechaEmision  = fechaEmision
        f.idHoja        = idHoja
        f.importeTotal  = importeTotal
        session.commit()

def lista_facturas_usuario(id_usuario):
    u = buscar_usuario(id_usuario)
    if(u!=False):
        facturas = session.query(Factura).filter(Factura.idUsuario == id_usuario).all()
        lista_facturas=[]
        for f in lista_facturas:
            lista_facturas.append(f)
        return lista_facturas
    else:
        return False



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
