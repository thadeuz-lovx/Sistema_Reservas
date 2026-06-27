from fastapi import APIRouter, Form, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from src.cliente.cruds import ClientCRUDs
from src.cliente.schemas import ClientUpdate

routing = APIRouter(prefix="/clientes", tags=["Clientes"])

@routing.post("/", status_code=status.HTTP_201_CREATED)
def creacion(
    db: Session = Depends(get_db),
    nombre: str = Form(...),
    apellido: str = Form(...),
    referencia: str = Form(...),
    email: str = Form(...),
    codigo: str = Form(...),
    estado: str = Form(...)
):
    return ClientCRUDs.crear(
        db=db, nombre=nombre, apellido=apellido, 
        referencia=referencia, email=email, 
        codigo=codigo, estado=estado
    )

@routing.get("/", status_code=status.HTTP_200_OK)
def ver(db: Session = Depends(get_db)):
    return ClientCRUDs.ver(db=db)

@routing.get("/{id_usr}", status_code=status.HTTP_200_OK)
def ver_id(id_usr: int, db: Session = Depends(get_db)):
    busqueda = ClientCRUDs.ver_por(db=db, id_usr=id_usr)
    if not busqueda:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return busqueda

@routing.patch("/{id_usr}", status_code=status.HTTP_200_OK)
def actualizar(
    id_usr: int,
    nombre: str = Form(None),
    apellido: str = Form(None),
    referencia: str = Form(None),
    email: str = Form(None),
    codigo: str = Form(None),
    estado: str = Form(None),
    db: Session = Depends(get_db)
):
    cliente_existente = ClientCRUDs.ver_por(db=db, id_usr=id_usr)
    if not cliente_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    
    user_upd = ClientUpdate(
        nombre=nombre, apellido=apellido, referencia=referencia,
        email=email, codigo=codigo, estado=estado
    )
    
    ClientCRUDs.actualizar(db=db, id_usr=id_usr, user_upd=user_upd)
    return {"message": "Cliente actualizado correctamente"}

@routing.delete("/{id_usr}", status_code=status.HTTP_200_OK)
def eliminar(id_usr: int, db: Session = Depends(get_db)):
    eliminado = ClientCRUDs.eliminar(id_usr=id_usr, db=db)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return {"message": "Cliente eliminado correctamente"}
