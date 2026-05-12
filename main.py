from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.db import init_db
from fastapi.middleware.cors import CORSMiddleware
from routes.voiture_routes import router as voiture_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = await init_db()
    yield
    client.close()
    print("MongoDB connection closed")

app = FastAPI(
    title="Auto-Agent API",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voiture_router)

@app.get("/")
async def root():
    return {"message": "Auto-Agent API is running! 🚗"}