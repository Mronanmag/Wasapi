from fastapi import FastAPI
from pydantic_settings import BaseSettings
from .utils import CORSMiddleware


class Settings(BaseSettings) :
    app_name : str = "WASAPI"
    admin_email : str = "ronanmagouroux@gmail.com"
    items_per_user : int = 50

settings = Settings()
app = FastAPI()

origins = [
    "http://localhost:8001",
    "localhost:8001",
    "http://10.4.5.59:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/info")
async def info() :
    return {
        "app_name" : settings.app_name, 
        "admin_email" : settings.admin_email,
        "items_per_user" : settings.items_per_user}

@app.get("/", tags=["root"])
async def read_root() :
    return {"message" : "Welcome to WASAPI"}
