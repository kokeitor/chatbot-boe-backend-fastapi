from fastapi import FastAPI, HTTPException
from decouple import config
from src.routes.routes import iaResponse
from src.Apis.openai_api import OpenAiModel
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


print(f"OPENAI_API_KEY : {config('OPENAI_API_KEY')}")
FRONT_END_URL = config('FRONT_END_URL')
print(f"FRONT_END_URL : {FRONT_END_URL}")
origins = [
    FRONT_END_URL
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the model in the state atribute of the app object
    app.state.AI_MODEL = OpenAiModel(api_ky=config('OPENAI_API_KEY'))
    yield
    # Clean up the model and release the resources
    app.state.AI_MODEL = None


app = FastAPI(
    title="Boe ChatBot BACKEND",
    lifespan=lifespan
)
app.include_router(iaResponse)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.get('/')
async def welcome():
    return {"response": "hola welcome!"}
