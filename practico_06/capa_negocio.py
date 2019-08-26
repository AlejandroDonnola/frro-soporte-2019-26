# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        oSoc=self.datos.buscar(id_socio)
        return oSoc

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        oSoc=self.datos.buscar_dni(dni_socio)
        return oSoc

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        socios=self.datos.todos()
        return socios

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_1(socio)
        except DniRepetido as e:
            print('Error:', e.args)
            return False
        try:
            self.regla_2(socio)
        except LongitudInvalida as e:
            print('Error:',e.args)
            return False
        try:
            self.regla_3()
        except MaximoAlcanzado as e:
            print('Error:',e.args)
            return False
        else:
            self.datos.alta(socio)
            return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        respuesta=self.datos.baja(id_socio)
        return respuesta

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_2(socio)
        except LongitudInvalida as e:
            print('Error:',e.args)
            return False
        else:
            self.datos.modificacion(socio)
            return True

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        oSoc = self.datos.buscar_dni(socio.DNI)
        if oSoc is not None:
            raise DniRepetido('DNI repetido')
        else:
            return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        x= len(socio.Nombre)
        y= len(socio.Apellido)
        if (x >= self.MIN_CARACTERES and x <= self.MAX_CARACTERES) and (y >=self.MIN_CARACTERES and y <= self.MAX_CARACTERES) :
            return True
        else:
            raise LongitudInvalida('Nombre o Apellido no tienen entre 3 y 15 caracteres')

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        socios=self.datos.todos()
        x=len(socios)
        if self.MAX_SOCIOS>x:
            return False
        else:
            raise MaximoAlcanzado('Se esta excediendo la cantidad maxima de socios')
