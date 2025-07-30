from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_crear_usuario_exitoso():
    payload = {"nombre": "Joel", "edad": 30}
    response = client.post("/usuario", json=payload)

    assert response.status_code == 200
    assert response.json() == {
        "mensaje": "Hola Joel, tienes 30 años."
    }

def test_crear_usuario_faltan_datos():
    payload = {"nombre": "Joel"}  # Falta la edad
    response = client.post("/usuario", json=payload)

    assert response.status_code == 422  # Error de validación Pydantic
 