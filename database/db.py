import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

async def init_db():
    MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "auto_agent_db")

    client = AsyncIOMotorClient(MONGO_URL)

    # Import here to avoid circular imports
    from models import all_models
    await init_beanie(database=client[DB_NAME], document_models=all_models)

    print(f"✅ Connected to MongoDB: {DB_NAME}")
    return client