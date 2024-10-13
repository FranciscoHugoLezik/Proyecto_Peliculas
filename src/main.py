from fastapi import FastAPI

from src.scripts import (root, 
                         cantidad_mes, 
                         cantidad_dia, 
                         score_titulo, 
                         votos_titulo, 
                         actor, 
                         director)


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