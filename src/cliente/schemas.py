from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientBase(BaseModel):
    nombre: str
    apellido: str
    referencia: str
    email: EmailStr
    estado: str
    codigo: str

class ClientMake(ClientMake):
    pass

class ClientUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    referencia: Optional[str] = None
    email: Optional[EmailStr] = None
    codigo: Optional[str] = None
    estado: Optional[str] = None

class ClientResponse(ClientBase):
    id: int

    class Config:
        from_attributes = True  # Permite a Pydantic leer modelos de SQLAlchemy