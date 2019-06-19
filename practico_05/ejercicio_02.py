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
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        return []

    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return False

    def alta(self, socio):
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio):
        oSoc = self.session.query(Socio).filter(Socio.IdSocio == id_socio).first()
        if oSoc is None:
            return False
        else:
            self.session.delete(oSoc)
            self.session.commit()
            return True

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        return socio


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
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
