# Implementar los metodos de la capa de negocio de socios.

from Practica05.ejercicio_01 import Socio
from Practica05.ejercicio_02 import DatosSocio


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
        oSoc=self.datos.buscar(id_socio)

        return oSoc

    def buscar_dni(self, dni_socio):
        oSoc=self.datos.buscar_dni(dni_socio)
        if oSoc is not None:
            return oSoc
        else:
            return None



    def todos(self):
        socios=self.datos.todos()
        return socios

    def alta(self, socio):
        try:
            self.regla_1(socio)
        except DniRepetido as e:
            print('Error:',e.args)
            return False

        try:
            self.regla_2(socio)
        except LongitudInvalida as e:
            print('Error:',e.args)
            return False

        try:
            self.regla_3(socio)
        except MaximoAlcanzado as e:
            print('Error:',e.args)
            return False

        else:
            self.datos.alta(socio)
            return True




        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        return False

    def baja(self, id_socio):
        respuesta=self.datos.baja(id_socio)
        return respuesta

    def modificacion(self, socio):
        try:
            self.regla_2(socio)
        except LongitudInvalida as e:
            print('Error:',e.args)
            return False
        else:
            self.datos.alta(socio)
            return True




        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """

    def regla_1(self, socio):
        oSoc = self.datos.buscar_dni(socio.DNI)
        if oSoc is not None:
            raise DniRepetido('DNI repetido')
            return False
        else:
            return True


        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """

        return False

    def regla_2(self, socio):
        x= len(socio.Nombre)
        y= len(socio.Apellido)
        if (x >= self.MIN_CARACTERES and x <= self.MAX_CARACTERES) and (y >=self.MIN_CARACTERES and y <= self.MAX_CARACTERES) :
            return True
        else:
            raise LongitudInvalida('Nombre o Apellido no tienen entre 3 y 15 caracteres')
            return false



        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """


    def regla_3(self):
        socios=self.datos.todos()
        x=len(socios)
        if  self.MAX_SOCIOS>x:
            return False
        else:
            raise MaximoAlcanzado('Se esta excediendo la cantidad maxima de socios')
            return True

        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """

