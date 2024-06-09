from database.models import Cars, CategoryCars
from database import get_db
from datetime import datetime


def get_car_db(id):
    db = next(get_db())
    car_info = db.query(Cars).filter_by(id=id).first()
    if car_info:
        return car_info
    return False


def delete_car_db(id):
    db = next(get_db())
    delete_car = db.query(Cars).filter_by(id=id).first()
    if delete_car:
        db.delete(delete_car)
        db.commit()
        return "Successfully deleted"
    return False


def change_car_db(id, new_car):
    db = next(get_db())
    change_car = db.query(Cars).filter_by(id=id).first()
    if change_car:
        change_car.model_of_car = new_car
        db.commit()
        return "Successfully changed!"
    return False


def add_car_db(id, model_of_car, type, id_detail, colour, strength_of_car, date_of_issue, amount_of_cars, description):
    db = next(get_db())
    new_car = Cars(id=id, model_of_car=model_of_car, type=type, reg_date=datetime.now())
    new_detail_car = CategoryCars(id_detail=id_detail, amount_of_cars=amount_of_cars, date_of_issue=date_of_issue,
                                  colour=colour, strength_of_car=strength_of_car, description=description,
                                  reg_date=datetime.now())
    db.add(new_car, new_detail_car)
    db.commit()
    return True


def get_all_cars():
    db = next(get_db())
    cars = db.query(Cars).all()
    return cars
