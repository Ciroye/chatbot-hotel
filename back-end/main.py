from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import db
from api import api_router
from domain.models.db.room import Room
from infraestructure.utils import Config

config = Config().get_config(section='app')

app = FastAPI(title=config['project_name'], openapi_url="/api/v1/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=config['api_url'])

if __name__ == '__main__':
    print("Migration Start")
    db.Base.metadata.create_all(db.engine)
