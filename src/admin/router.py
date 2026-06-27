from fastapi import APIRouter, status, HTTPException, Depends, Form
from backend.database import get_db
from backend.models.admin import AdminSave
from src.admin.cruds import AdminCRUDs
from sqlalchemy.orm import Session
from typing import Optional
from src.admin.schemas import AdminUptdate
routing = APIRouter(prefix="/admin", tags=["Administrador"])

@routing.post("/", status_code=status.HTTP_201_CREATED)
def crear(
    db: Session = Depends(get_db),
    nombre: str = Form(...),
    apellido: str = Form(...),
    estado: str = Form(...)
):
    nuevo_admin = AdminCRUDs.crear_a(db=db, nombre=nombre, apellido=apellido, estado=estado)
    return nuevo_admin

@routing.get("/", status_code=status.HTTP_200_OK)
def ver(
    db: Session = Depends(get_db),
):
    busqueda = AdminCRUDs.ver_admins(db=db)
    return busqueda

@routing.get("/{id_adm}", status_code=status.HTTP_200_OK)
def ver_id(
    id_adm: int,
    db: Session = Depends(get_db)
):
    busqueda = AdminCRUDs.ver_admin_id(
        db=db,
        id_adm=id_adm
    )

    if not busqueda:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return busqueda

@routing.patch("/{id_adm}", status_code=status.HTTP_200_OK)
def actualizar(
    id_adm: int,
    db: Session = Depends(get_db),
    nombre: Optional[str] = Form(None),
    apellido: Optional[str] = Form(None),
    estado: Optional[str] = Form(None)
):
    datos_limpios = {
        k: v for k, v in {"nombre": nombre, "apellido": apellido, "estado": estado}.items()
        if v is not None
    }

    update_schema = AdminUptdate(**datos_limpios)

    datos_actualizados = AdminCRUDs.actualizar_adm(
        db=db,
        id_adm=id_adm,
        admin_update=update_schema
    )

    if not datos_actualizados:
        raise HTTPException(status_code=404, detail="User no actualizado")
    return datos_actualizados

@routing.delete("/{id_adm}", status_code=status.HTTP_200_OK)
def eliminar(id_adm: int, db: Session = Depends(get_db)):
    eliminar = AdminCRUDs.borrar_adm(db=db, id_adm=id_adm)

    if not eliminar:
        raise HTTPException(status_code=404, detail="Not found")
    
    return True
