from fastapi import APIRouter, status, HTTPException, Depends, Form
from backend.database import get_db
from sqlalchemy.orm import Session
from src.profesional.cruds import ProfessionalCRUDs
from src.profesional.schemas import ProfessionalUptade
from typing import Optional

routing = APIRouter(prefix="/profesionales", tags=["Profesionales"])

@routing.post("/", status_code=status.HTTP_201_CREATED)
def creacion(
    db: Session = Depends(get_db),
    nombre: str = Form(...),
    apellido: str = Form(...),
    especialidad: str = Form(...),
    codigo: str = Form(...),
    estado: str = Form(...)
):
    profesional = ProfessionalCRUDs.crear(
        db=db, nombre=nombre, apellido=apellido,
        especialidad=especialidad, codigo=codigo, estado=estado
    )

    if not profesional:
        raise HTTPException(status_code=500, detail="Internal problem server")
    
    return profesional

@routing.get("/", status_code=status.HTTP_200_OK)
def ver(
    db: Session = Depends(get_db)
):
    return ProfessionalCRUDs.ver(db=db)

@routing.get("/{id_prf}", status_code=status.HTTP_200_OK)
def ver_id(
    id_prf: int,
    db: Session = Depends(get_db)
):
    profesional = ProfessionalCRUDs.ver_id(
        db=db, id_prf=id_prf
    )

    if not profesional:
        raise HTTPException(status_code=404, detail="Not found")
    
    return profesional


@routing.patch("/{id_prf}", status_code=status.HTTP_200_OK)
def actualizar(
    id_prf: int,
    db: Session = Depends(get_db),
    nombre: Optional[str] = Form(None),
    apellido: Optional[str] = Form(None),
    especialidad: Optional[str] = Form(None),
    codigo: Optional[str] = Form(None),
    estado: Optional[str] = Form(None)
):
    busqueda = ProfessionalCRUDs.ver_id(db=db, id_prf=id_prf)
    if not busqueda:
        raise HTTPException(status_code=404, detail="Not found")
    
    campos_recibidos = {
        "nombre": nombre,
        "apellido": apellido,
        "especialidad": especialidad,
        "codigo": codigo,
        "estado": estado
    }
    
    datos_actualizar = {k: v for k, v in campos_recibidos.items() if v is not None}

    if not datos_actualizar:
        raise HTTPException(status_code=400, detail="No se enviaron campos para modificar")

    actualizacion = ProfessionalCRUDs.actualizar(
        db=db, id_prf=id_prf, datos=datos_actualizar
    )

    if not actualizacion:
        raise HTTPException(status_code=404, detail="Usuario no actualizado")

    return actualizacion

@routing.delete("/{id_prf}", status_code=status.HTTP_200_OK)
def eliminar(
    id_prf: int,
    db: Session = Depends(get_db),
):
    eliminacion = ProfessionalCRUDs.borrar(db=db, id_prf=id_prf)
    if not eliminacion:
        raise HTTPException(status_code=404, detail="Not found")
    
    return True