from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Gestor de Gastos")

templates = Jinja2Templates(directory="templates")

class Gasto(BaseModel):
    descripcion: str
    categoria: str
    monto: float

gastos: List[Gasto] = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    total = sum(g.monto for g in gastos)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "gastos": gastos, "total": total}
    )

@app.post("/gastos")
def crear_gasto(gasto: Gasto):
    gastos.append(gasto)
    return {"mensaje": "Gasto registrado"}
