from pydantic import BaseModel
from typing import Optional

class ProfessionalBase(BaseModel):
    nombre: str
    apellido: str
    especialidad: str
    codigo: str
    estado: str

class ProfessionalMake(ProfessionalBase):
    pass

class ProfessionalUptade(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    especialidad: Optional[str] = None
    codigo: Optional[str] = None
    estado: Optional[str] = None

class ProfessionaResponse(ProfessionalBase):
    id: int

    class Config:
        from_attributes = True

