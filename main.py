from fastapi import FastAPI
from pydantic import BaseModel
import requests
# Instancia de la aplicación
app = FastAPI()

# Modelo de datos para POST
class Usuario(BaseModel):
    nombre: str
    edad: int

# Ruta de prueba (GET)
@app.get("/")
def inicio():
    return {"mensaje": "API lista"}

# Ruta para recibir datos (POST)
@app.post("/usuario")
def crear_usuario(usuario: Usuario):
    return {
        "mensaje": f"Hola {usuario.nombre}, tienes {usuario.edad} años."
    }

# Ruta local que consulta una API externa
@app.get("/buscar-post/{post_id}")
def obtener_post(post_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return {
            "titulo": datos["title"],
            "contenido": datos["body"]
        }
    else:
        return {"error": f"No se pudo obtener el post con ID {post_id}"}