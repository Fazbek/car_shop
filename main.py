from fastapi import FastAPI
from api.car_api.car import car_router
from database import Base, engine


app = FastAPI(docs_url="/")
Base.metadata.create_all(bind=engine)


app.include_router(car_router)
