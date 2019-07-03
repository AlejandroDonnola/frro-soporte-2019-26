# Implementar los metodos de la capa de datos de socios.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, id_socio):
        oSoc = self.session.query(Socio).filter(Socio.IdSocio == id_socio).first()
        return oSoc

    def buscar_dni(self, dni_socio):
        oSoc = self.session.query(Socio).filter(Socio.DNI == dni_socio).first()
        return oSoc

    def todos(self):
        socios= self.session.query(Socio).all()
        return socios

    def borrar_todos(self):
        self.session.query(Socio).delete()
        self.session.commit()
        return True

    def alta(self, socio):
        oSoc = Socio(DNI=socio.DNI, Nombre=socio.Nombre, Apellido=socio.Apellido)
        self.session.add(oSoc)
        self.session.commit()
        return oSoc

    def baja(self, id_socio):
        oSoc = self.buscar(id_socio)
        if oSoc is not None:
            self.session.delete(oSoc)
            self.session.commit()
            return True
        else:
            return False

    def modificacion(self, socio):
        oSoc = self.buscar(socio.IdSocio)
        if oSoc is not None:
            oSoc.Nombre = socio.Nombre
            oSoc.Apellido = socio.Apellido
            oSoc.DNI = socio.DNI
            self.session.commit()
        return oSoc


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(DNI=12345678, Nombre='Juan', Apellido='Perez'))
    assert socio.IdSocio > 0
    
    # baja
    assert datos.baja(socio.IdSocio) is True

    # buscar
    socio_2 = datos.alta(Socio(DNI=12345679, Nombre='Carlos', Apellido='Perez'))
    assert datos.buscar(socio_2.IdSocio) == socio_2

    # buscar dni
    assert datos.buscar_dni(socio_2.DNI) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(DNI=12345680, Nombre='Susana', Apellido='Gimenez'))
    socio_3.Nombre = 'Moria'
    socio_3.Apellido = 'Casan'
    socio_3.DNI = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.IdSocio)
    assert socio_3_modificado.IdSocio == socio_3.IdSocio
    assert socio_3_modificado.Nombre == 'Moria'
    assert socio_3_modificado.Apellido == 'Casan'
    assert socio_3_modificado.DNI == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
