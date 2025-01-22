from motor.motor_asyncio import AsyncIOMotorClient

#Mongo URI
MONGO_URI = "mongodb://<username>:<password>@cluster0.j7zn5.mongodb.net/"
client = AsyncIOMotorClient(MONGO_URI)
db = client["test"] # Database name