from fastapi import FastAPI, HTTPException
from decouple import config
from src.routes.routes import iaResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(iaResponse)

FRONT_END_URL = config('FRONT_END_URL')
print(f"FRONT_END_URL : {FRONT_END_URL}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def welcome():
    return {"response": "hola welcome!"}



