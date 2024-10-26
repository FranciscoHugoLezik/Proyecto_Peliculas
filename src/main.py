from fastapi import FastAPI

from src.scripts.credits import actor, director
from src.scripts.movies import cantidad_dia, cantidad_mes, score_titulo, votos_titulo
from src.scripts import (root)


app = FastAPI()

routers = (
    root.router, 
    cantidad_mes.router, 
    cantidad_dia.router, 
    score_titulo.router, 
    votos_titulo.router, 
    actor.router, 
    director.router
)
for router in routers:
    app.include_router(router)