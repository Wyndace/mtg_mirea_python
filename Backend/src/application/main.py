import uvicorn
from fastapi import FastAPI

from Backend.src.application.controllers.http import routers

app = FastAPI(
    title="MTG Api for RTU MIREA",
    version="v1",
)

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
