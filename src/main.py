from fastapi import FastAPI, Request
from fastapi_jwt_auth.exceptions import AuthJWTException
from starlette.responses import JSONResponse

from src.routers import maps, login

app = FastAPI()
app.include_router(maps.router)
app.include_router(login.router)


@app.get('/')
async def health_check():
    return {'message': 'healthy!'}


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(_: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
