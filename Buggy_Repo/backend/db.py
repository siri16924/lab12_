from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging

def init_db():
    try:
        MONGO_URI = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client["testdb"]

        # Attempt a test command to ensure connection works
        client.admin.command('ping')

        return {
            "items_collection": db["item"],
            "users_collection": db["users"]
        }

    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        return None
