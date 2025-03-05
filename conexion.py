import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Variable que guarda la URL de conexión a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:123@localhost/servrest_db")

# Objeto de tipo SQLalchemy que utiliza como parametro la url para realizar la conexion a la db
engine = create_engine(DATABASE_URL)

# Configura la sesión para interactuar con la BD
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Declaración Base para los modelos ORM
Base = declarative_base()