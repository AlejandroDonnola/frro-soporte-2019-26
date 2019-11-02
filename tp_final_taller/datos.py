from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Float, Date, ForeignKey,Boolean,FLOAT
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.engine import create_engine



Base = declarative_base()
engine = create_engine('mysql://root:852456ale@localhost:3306/python')
Base.metadata.bind = engine


class Rol(Base):
    __tablename__ = 'roles'
    id_rol      = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(80), nullable=False)
    usuarios    = relationship("Usuario")


class Usuario(Base):
    __tablename__ = 'usuarios'
    id_usuario  = Column(Integer, primary_key=True, autoincrement=True)
    id_rol      = Column(Integer, ForeignKey('roles.id_rol'), nullable=False)
    nombre      = Column(String(30), nullable=False)
    apellido    = Column(String(30), nullable=False)
    dni         = Column(Integer, nullable=False, unique=True)
    email       = Column(String(30), nullable=False, unique=True)
    password    = Column(String(30), nullable=False)
    tel         = Column(Integer, nullable=True)
    habilitado  = Column(Boolean, nullable=False)
    autos       = relationship("Auto")
    reparaciones= relationship("Reparacion")
    hojas       = relationship("HojaDeParte")
    factura     = relationship("Factura")


class Auto(Base):
    __tablename__ = 'autos'
    id_patente = Column(String(30), primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    marca      = Column(String(30), nullable=False)
    modelo     = Column(String(30), nullable=False)
    color      = Column(String(30), nullable=False)
    reparaciones = relationship("Reparacion")
    hojas        = relationship("HojaDeParte")


class Repuesto(Base):
    __tablename__    = 'repuestos'
    id_repuesto     = Column(Integer, primary_key=True, autoincrement=True)
    id_tipo_repuesto = Column(Integer,ForeignKey('tipoderepuestos.id_tipoderepuesto'))
    descripcion      = Column(String(30), nullable=False)
    stock            = Column(Integer, nullable=False)
    punto_pedido     = Column(Integer, nullable=True)
    precio_unitario  = Column(FLOAT, nullable=False)



class HojaDeParte(Base):
    __tablename__      = 'hojasdeparte'
    id_hoja            = Column(Integer, primary_key=True, autoincrement=True)
    id_factura         = Column(Integer, ForeignKey('facturas.id_factura'), nullable=False)
    id_mecanico        = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    id_patente         = Column(String(30), ForeignKey('autos.id_patente'), nullable=False)
    costo_mano_de_obra = Column(FLOAT, nullable=False)


class Factura(Base):
    __tablename__   = 'facturas'
    id_factura      = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario      = Column(Integer, ForeignKey('usuarios.id_usuario'))
    fecha_emision   = Column(Date, nullable=False)
    importe_total   = Column(FLOAT, nullable=False)
    hoja            = relationship("HojaDeParte")



class Reparacion(Base):
    __tablename__ = 'reparaciones'
    id_reparacion        = Column(Integer, unique=True, autoincrement=True)
    id_patente           = Column(String(10), ForeignKey('autos.id_patente'))
    id_mecanico          = Column(Integer, ForeignKey('usuarios.id_usuario'))
    fecha_ingreso        = Column(Date, nullable=False)
    fecha_salida         = Column(Date, nullable=False)
    estado_reparacion    = Column(String(40), nullable=False)
    PrimaryKeyConstraint(id_patente,id_mecanico,fecha_ingreso)


class Proveedor(Base):
    __tablename__ = 'proveedores'
    id_cuit      = Column(Integer,primary_key=True, unique=True)
    razon_social = Column(String(30), nullable=False)
    tel          = Column(String(30), nullable=True)
    direccion    = Column(String(30), nullable=True)
    email        = Column(String(30), nullable=False)

class Tipo_Repuesto(Base):
    __tablename__    = 'tipoderepuestos'
    id_tipoderepuesto  = Column(Integer,primary_key=True, unique=True)
    descripcion      = Column(String(30), nullable=False)
    repuesto    = relationship("Repuesto")



hoja_repuesto = Table('hojaRepuesto', Base.metadata,
            Column('id_repuesto',Integer, ForeignKey('repuestos.id_repuesto')),
            Column('id_hoja', Integer, ForeignKey('hojasdeparte.id_hoja')),
            Column('cantidad', Integer),
            Column('precio_total',FLOAT))


proveedor_repuesto = Table('proveedorRepuesto', Base.metadata,
            Column('cuit_proveedor', Integer, ForeignKey('proveedores.id_cuit')),
            Column('id_repuesto', Integer, ForeignKey('repuestos.id_repuesto')))


Base.metadata.create_all(engine)
