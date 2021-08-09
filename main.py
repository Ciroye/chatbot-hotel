from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from infraestructure.generic import DbFactory
from domain.services.auth import AuthService
from infraestructure.utils import Config
from starlette.requests import Request
from fastapi import FastAPI, Depends
from domain.models import Token
from api import api_router

config = Config().get_config(section='app')

app = FastAPI(title=config['proyect_name'], openapi_url="/api/v1/openapi.json")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=config['api_url'])
