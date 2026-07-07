from src.cliente.schemas import ClientUpdate
from backend.models.cliente import ClientSave
from sqlalchemy.orm import Session
from sqlalchemy import select
class ClientCRUDs:
    @staticmethod
    def crear(
        db: Session,  
        nombre: str,
        apellido: str,
        referencia: str,
        email: str,
        estado: str,
        codigo: str,
        password_plano: str
    ):
        
        
        nuevo_usuario = ClientSave(
            nombre=nombre,
            apellido=apellido,
            referencia=referencia,
            email=email,
            estado=estado,
            codigo=codigo,
        )

        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
        return nuevo_usuario
    
    @staticmethod
    def ver(db: Session):
        # 3. SQLAlchemy Async no soporta db.query(). Usamos select() ejecutado con await
        resultado =  db.execute(select(ClientSave))
        return resultado.scalars().all()
    
    @staticmethod
    async def ver_por(db: Session, id_usr: int):
        resultado =  db.execute(select(ClientSave).filter(ClientSave.id == id_usr))
        busqueda = resultado.scalar_one_or_none()

        if not busqueda:
            return None
        
        return busqueda

    @staticmethod
    def actualizar(db: Session, id_usr: int, user_upd: ClientUpdate):
        # Reutilizamos la lógica asíncrona para buscar primero
        resultado =  db.execute(select(ClientSave).filter(ClientSave.id == id_usr))
        busqueda = resultado.scalar_one_or_none()

        if not busqueda:
            return None
        
        actualizar_usuario = user_upd.model_dump(exclude_unset=True)

        for k, v in actualizar_usuario.items():
            setattr(busqueda, k, v)

        db.commit()
        db.refresh(busqueda)
        return busqueda
    
    @staticmethod
    def eliminar(db: Session, id_usr: int):
        resultado =  db.execute(select(ClientSave).filter(ClientSave.id == id_usr))
        busqueda = resultado.scalar_one_or_none()

        if not busqueda:
            return None
        
        # db.delete() prepara la eliminación en memoria, pero el commit la ejecuta en la BD
        db.delete(busqueda)
        db.commit()

        return True
