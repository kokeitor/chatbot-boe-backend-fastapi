from fastapi import FastAPI, HTTPException
from decouple import config
from src.routes.routes import iaResponse
from fastapi.middleware.cors import CORSMiddleware

FRONT_END_URL = config('FRONT_END_URL')
print(f"FRONT_END_URL : {FRONT_END_URL}")
origins = [
    FRONT_END_URL
]

app = FastAPI()
app.include_router(iaResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST","GET"],
    allow_headers=["*"],
)

@app.get('/')
async def welcome():
    return {"response": "hola welcome!"}



