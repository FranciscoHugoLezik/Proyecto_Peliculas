from fastapi import FastAPI

from src.scripts.credits import (get_actor, 
                                 get_director)
from src.scripts.movies import (cantidad_filmaciones_dia, 
                                cantidad_filmaciones_mes, 
                                score_titulo, 
                                votos_titulo)
from src.scripts import (root)


app = FastAPI()

routers = (
    root.router, 
    cantidad_filmaciones_mes.router, 
    cantidad_filmaciones_dia.router, 
    score_titulo.router, 
    votos_titulo.router, 
    get_actor.router, 
    get_director.router
)
for router in routers:
    app.include_router(router)