from pydantic import BaseModel
from typing import Optional

class AdminModel(BaseModel):
    nombre: str
    apellido: str
    estado: str

class AdminMake(AdminModel):
    pass 

class AdminUptdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    estado: Optional[str] = None

class AdminResponse(AdminModel):
    id: int

