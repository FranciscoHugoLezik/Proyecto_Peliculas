from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter()

@router.get("/", 
            response_class=HTMLResponse)
async def root():
    datos_del_autor = {
        "Autor": "Francisco Hugo Lezik",
        "Curso": "Curso de Ciencia de Datos de Henry, cohorte 10"
    }
    mapa_del_sitio = {
        "/": "Pagina principal",
        "/cantidad_mes/mes": """Retorna la cantidad de peliculas 
                             estrenadas en un determinado mes 
                             escrito en español.""",
        "/cantidad_dia/dia": """Retorna la cantidad de peliculas 
                             estrenadas en un determinado dia 
                             escrito en español.""",
        "/score_titulo/titulo": """Retorna el titulo de la pelicula, 
                                el año en que fue estrenada y su 
                                popularidad.""",
        "/votos_titulo/titulo": """Retorna el titulo de la pelicula, 
                                el año en que fue estrenada, la 
                                cantidad de votos y el promedio 
                                de votos.""",
        "/actor/nombre": """Retorna el nombre del actor, la cantidad de 
                         peliculas en las que participo, la cantidad 
                         que tiene retorno, el retorno total y el 
                         retorno promedio.""",
        "/director/nombre": """Retorna el nombre del director, la 
                            cantidad de peliculas que dirigio, la 
                            cantidad que tiene retorno y el retorno 
                            total. Ademas retorna el nombre de cada 
                            pelicula, su fecha de estreno, su retorno 
                            individual, su costo y su ganancia."""
    } 
    precondicion = {
        "Precondicion": """Los titulos y nombres deben estar escritos, respetando 
                        las mayusculas y minusculas, como estan en el dataset."""
    }
    html_content = "<html><body>"
    html_content += "<p><strong>Proyecto Individual MVP de un Sistema \n"
    html_content += "de Recomendación de Peliculas</strong></p>"
    html_content += "<br><br>"
    
    for key, value in datos_del_autor.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "<br><br>"
    
    html_content += "<p><strong>Mapa del sitio:</strong></p>"
    for key, value in mapa_del_sitio.items():
        html_content += f"<p><strong>{key}:</strong> {value}</p>"
    html_content += "<br><br>"        

    html_content += f"<p><strong>Precondicion:</strong> \n"
    html_content += f"{precondicion['Precondicion']}</p>"
    html_content += "</body></html>"
    
    return (HTMLResponse(content=html_content))