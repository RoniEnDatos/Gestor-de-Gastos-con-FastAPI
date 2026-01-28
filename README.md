# Gestor de Gastos con FastAPI

Proyecto personal desarrollado para practicar el uso de FastAPI y la creación de aplicaciones web simples con Python.

## Descripción
Esta aplicación permite registrar gastos mediante un formulario web y mostrarlos en pantalla. 
Está pensada como un proyecto de aprendizaje para entender cómo funciona un backend ligero con FastAPI y renderizado de HTML.

## Tecnologías utilizadas
- Python
- FastAPI
- HTML
- Jinja2
- Uvicorn

## Funcionamiento de la aplicación
- El usuario ingresa un monto y una descripción del gasto desde un formulario HTML.
- El backend recibe los datos usando FastAPI.
- Los gastos se almacenan en memoria (lista de Python).
- Los datos se envían nuevamente al HTML para mostrarlos al usuario.

## Qué aprendí con este proyecto
- Crear endpoints GET y POST con FastAPI.
- Recibir datos desde formularios HTML.
- Renderizar plantillas HTML usando Jinja2.
- Separar la lógica backend de la vista.
- Ejecutar aplicaciones FastAPI con Uvicorn.

## Instalación y ejecución
1. Instalar dependencias:
```bash
pip install -r requirements.txt

