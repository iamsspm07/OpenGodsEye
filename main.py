from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="GodsEye AI Tracker")

app.include_router(router)