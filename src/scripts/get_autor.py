from fastapi import APIRouter


router = APIRouter()


@router.get("/get_project_autor")
async def get_project_autor() -> dict:
    """Retorna los datos del autor.
    
    Return: 
    
    dict: es un texto con los datos.
    """
    respuesta = {
        "Proyecto": "Sistema de Recomendación de Películas", 
        "Autor": "Francisco Hugo Lezik",
        "Academia": "Henry", 
        "Curso": "Data Science Part Time", 
        "Cohorte": "11"
        }
    return respuesta