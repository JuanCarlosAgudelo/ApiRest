from pydantic import BaseModel
from tablas import Computadores


class ComputadorBase(BaseModel):
    referencia: str
    marca: str
    cpu: str
    ram: int
    almacenamiento: int

class ComputadorRespuesta(ComputadorBase):
    referencia: str

    class Config:
        from_atributes = True



class AlmacenBase(BaseModel):
    referencia_comp: str
    cantidad: int

class AlmacenRespuesta(AlmacenBase):
    referencia_comp: str

    class Config:
        from_atributes = True