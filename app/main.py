from fastapi import FastAPI
from sqlalchemy.orm import Session
from db.db_engine import engine
from fastapi.middleware.cors import CORSMiddleware
from api.terms import term_router
from api.links import link_router
from db.models import Base
from config import config
import uvicorn 


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(term_router, prefix="/api")
app.include_router(link_router, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)