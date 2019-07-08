# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.engine import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///socios.db')


class Socio(Base):
    __tablename__ = 'socios'
    IdSocio = Column(Integer, primary_key=True, autoincrement=True)
    DNI = Column(Integer, nullable=False, unique=True)
    Nombre = Column(String(250), nullable=False)
    Apellido = Column(String(250), nullable=False)


Base.metadata.create_all(engine)
    # id = Column(...)
    # dni = Column(...)
    # nombre = Column(...)
    # apellido = Column(...)
