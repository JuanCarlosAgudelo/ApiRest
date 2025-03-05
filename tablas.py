from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from conexion import Base, engine  # Importamos el objeto de tipo declarative_base()

# Modelo Computadores
class Computadores(Base):
    __tablename__ = "computadores"

    id = Column(Integer, primary_key=True, autoincrement=True)  # PK en ID
    referencia = Column(String, unique=True, index=True, nullable=False)
    marca = Column(String, nullable=False)
    cpu = Column(String, nullable=False)
    ram = Column(Integer, nullable=False)
    almacenamiento = Column(Integer, nullable=False)

    almacen = relationship("Almacen", back_populates="computador", uselist=False)  # Relación 1 a 1

# Modelo Almacen
class Almacen(Base):
    __tablename__ = "almacen"

    id = Column(Integer, primary_key=True, autoincrement=True)  # PK en ID
    referencia_comp = Column(String, ForeignKey("computadores.referencia"), unique=True, nullable=False)
    cantidad = Column(Integer, nullable=False)

    computador = relationship("Computadores", back_populates="almacen")  # Relación con Computadores