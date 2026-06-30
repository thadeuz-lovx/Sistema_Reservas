from src.cliente.router import routing as clientes
from src.admin.router import routing as admin
from src.profesional.router import routing as profesionales
from fastapi import FastAPI

app = FastAPI(
    title="Mi API de Profesionales",
    version="1.0.0"
)

app.include_router(profesionales)
app.include_router(clientes)
app.include_router(admin)

@app.get("/")
def inicio():
    return {"message": "Bienvenido a la API Principal"}

# Esto permite ejecutar el archivo directamente con: python main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)