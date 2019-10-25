from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.engine import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///taller.db')


class Rol(Base):
    __tablename__ = 'roles'
    codRol = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(80), nullable=False)
    usuarios = relationship("Usuario")


class Usuario(Base):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    dni = Column(String(30), nullable=False, unique=True)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(String(30), nullable=False)
    tel = Column(String(30), nullable=True)
    codRol = Column(Integer, ForeignKey('roles.codRol'), nullable=False)
    habilitado = Column(String(30), nullable=False)
    autos = relationship("Auto")
    reparaciones = relationship("Reparacion")
    hojas = relationship("HojaDeParte")


class Auto(Base):
    __tablename__ = 'autos'
    idAuto = Column(Integer, unique=True, autoincrement=True)
    patente = Column(String(30), primary_key=True)
    marca = Column(String(30), nullable=False)
    modelo = Column(String(30), nullable=False)
    color = Column(String(30), nullable=False)
    idCliente = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    reparaciones = relationship("Reparacion")
    hojas = relationship("HojaDeParte")


class Repuesto(Base):
    __tablename__ = 'repuestos'
    idRepuesto = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(30), nullable=False)
    stock = Column(Integer, nullable=False)
    ptoPedido = Column(Integer, nullable=True)
    precio_unitario = Column(Float, nullable=False)


class HojaDeParte(Base):
    __tablename__ = 'hojas'
    idHoja = Column(Integer, primary_key=True, autoincrement=True)
    idMecanico = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    patente = Column(String(30), ForeignKey('autos.patente'), nullable=False)
    costo_manoDeObra = Column(Float, nullable=False)
    idRepuesto = Column(Integer, ForeignKey('repuestos.idRepuesto'), nullable=True)
    cantidad = Column(Integer, nullable=False)


class Factura(Base):
    __tablename__ = 'facturas'
    idFactura = Column(Integer, primary_key=True, autoincrement=True)
    fechaEmision = Column(Date, nullable=False)
    idHoja = Column(Integer, ForeignKey('hojas.idHoja'), nullable=False)
    importeTotal = Column(Float, nullable=False)


class Reparacion(Base):
    __tablename__ = 'reparaciones'
    idReparacion = Column(Integer, unique=True, autoincrement=True)
    patente = Column(Integer, ForeignKey('autos.idAuto'))
    idMecanico = Column(Integer, ForeignKey('usuarios.idUsuario'))
    fechaIngreso = Column(Date, nullable=False)
    fechaSalida = Column(Date, nullable=False)
    estado = Column(String(40), nullable=False)
    PrimaryKeyConstraint(patente,idMecanico,fechaIngreso)


class Proveedor(Base):
    __tablename__ = 'proveedores'
    idProveedor = Column(Integer, unique=True, autoincrement=True)
    cuit = Column(String(30), primary_key=True)
    razonSocial = Column(String(30), nullable=False)
    tel = Column(String(30), nullable=True)
    direccion = Column(String(30), nullable=True)
    email = Column(String(30), nullable=False)


proveedor_repuesto = Table('proveedorRepuesto', Base.metadata,
            Column('cuit_proveedor', String(30), ForeignKey('proveedores.cuit')),
            Column('id_repuesto', Integer, ForeignKey('repuestos.idRepuesto'))
                           )


Base.metadata.create_all(engine)

