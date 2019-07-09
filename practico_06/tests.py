# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida,DniRepetido,MaximoAlcanzado


cclass TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(DNI=12345678,Nombre='Juan', Apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)
        # valida regla
        valido = Socio(DNI=12345678, Nombre='Juan', Apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))
        #precondicion alta
        socio = Socio(DNI=12345678,Nombre='Juan', Apellido='Perez')
        exito = self.ns.alta(socio)
        # repetido
        invalido=Socio(DNI=12345678, Nombre='Juan', Apellido='Perez')
        self.assertFalse(self.ns.alta(invalido))
        self.assertRaises(DniRepetido,self.ns.regla_1,invalido)


    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(DNI=12345678, Nombre='Juan', Apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(DNI=12345678, Nombre='J', Apellido='Perez')
        self.assertFalse(self.ns.alta(invalido))
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
         # valida regla
        valido = Socio(DNI=12345678, Nombre='Juan', Apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(DNI=12345678, Nombre='JuanJuanJuanJuan', Apellido='Perez')
        self.assertFalse(self.ns.alta(invalido))
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(DNI=12345678, Nombre='Juan', Apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(DNI=12345678, Nombre='Juan', Apellido='Pe')
        self.assertFalse(self.ns.alta(invalido))
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(DNI=12345678, Nombre='Juan', Apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor 15 caracteres
        invalido = Socio(DNI=12345678, Nombre='Juan', Apellido='PerezPerezPerezPerez')
        self.assertFalse(self.ns.alta(invalido))
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)
        #max_socios=2
        self.ns.MAX_SOCIOS=2
        #1 SOCIO
        socio1 = Socio(DNI=123456738,Nombre='Juanx', Apellido='Perez')
        self.assertTrue(self.ns.alta(socio1))
        #2 SOCIO
        socio2 = Socio(DNI=123456038,Nombre='Juandx', Apellido='Pereez')
        self.assertTrue(self.ns.alta(socio2))
        #se comprueba si se registraron..
        self.assertEqual(len(self.ns.todos()), 2)

       #3 comprobar 3er SOCIO
        socio3 = Socio(DNI=125456038,Nombre='Juandx', Apellido='Pereez')
        self.assertFalse(self.ns.alta(socio3))
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)





    def test_baja(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)
        #probar eliminar socio sin estar dado de alta
        socio = Socio(DNI=123456738,Nombre='Juanx', Apellido='Perez')
        self.assertFalse(self.ns.baja(socio.IdSocio))


        # registrar 1 socio
        exito=self.ns.alta(socio)
        self.assertTrue(exito)

        # post-condiciones: 1 socio registrado
        self.assertEqual(len(self.ns.todos()), 1)
        # comprobar baja
        self.assertTrue(self.ns.baja(socio.IdSocio))





    def test_buscar(self):
        #alta a 1 socio
        socio = Socio(DNI=133636678,Nombre='Juan', Apellido='Perez')
        exito = self.ns.alta(socio)
        # post-condiciones: 1 socio registrado
        self.assertEqual(len(self.ns.todos()), 1)

        #buscar socio no valido
        assert self.ns.buscar(11111) is False
         #buscar socio valido
        assert self.ns.buscar(118) is True


    def test_buscar_dni(self):
        #alta a 1 socio
        socio = Socio(DNI=1234566878,Nombre='Juan', Apellido='Perez')
        exito = self.ns.alta(socio)
        # post-condiciones: 1 socio registrado
        self.assertEqual(len(self.ns.todos()), 1)

        #buscar socio no valido
        assert self.ns.buscar_dni(11111) is False
         #buscar socio valido
        assert self.ns.buscar_dni(1234566878) is True


    def test_todos(self):
        #alta a 1 socio
        socio = Socio(DNI=12345678,Nombre='Juan', Apellido='Perez')
        exito = self.ns.alta(socio)
        # post-condiciones: 1 socio registrado
        self.assertEqual(len(self.ns.todos()), 1)


    def test_modificacion(self):
       # nombre < a 3 caracteres
       invalido = Socio(DNI=12345678,Nombre='J', Apellido='Perez')
       self.assertFalse(self.ns.modificacion(invalido))
       # valido
       valido = Socio(DNI=12345678,Nombre='Juan', Apellido='Perez')
       self.assertTrue(self.ns.modificacion(valido))
