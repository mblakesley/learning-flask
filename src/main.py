from fastapi import FastAPI

from src.routers import maps

app = FastAPI()
app.include_router(maps.router)


@app.get('/')
async def health_check():
    return {'message': 'healthy!'}
