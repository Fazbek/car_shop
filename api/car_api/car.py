from fastapi import APIRouter
from database.carservice import get_car_db, delete_car_db, get_all_cars, add_car_db, change_car_db


car_router = APIRouter(prefix='/car', tags=["API for cars"])


@car_router.get('/get-car')
async def get_car(id: int):
    return f"The car: {get_car_db(id)}"


@car_router.get('/delete-car')
async def delete_car(id: int):
    return delete_car_db(id)


@car_router.get("/get-all-cars")
async def all_cars():
    return get_all_cars()


@car_router.get("/add-car")
async def add_car(id: int, model_of_car: str, type: str, id_detail: int, colour: str, strength_of_car: int, date_of_issue: int, amount_of_cars: int, description: str):
    add_c = add_car_db(id, model_of_car, type, id_detail, colour, strength_of_car, date_of_issue, amount_of_cars, description)
    return add_c


@car_router.get("/change-car")
async def change_car(id: int, new_car: str):
    return change_car_db(id, new_car)