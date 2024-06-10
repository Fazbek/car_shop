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
    return "Car not found"


def change_car_db(id, model_of_car, type):
    db = next(get_db())
    car = db.query(Cars).filter_by(id=id).first()
    if car:
        car.model_of_car = model_of_car
        car.type = type
        car.datetime = datetime.utcnow()
        db.commit()
        return "Successfully changed!"
    return "Car not found"


def add_car_db(id, model_of_car, type, id_detail, colour, strength_of_car, date_of_issue, amount_of_cars, description):
    db = next(get_db())
    new_car = Cars(id=id, model_of_car=model_of_car, type=type, reg_date=datetime.now())
    new_detail_car = CategoryCars(id_detail=id_detail, amount_of_cars=amount_of_cars, date_of_issue=date_of_issue,
                                  colour=colour, strength_of_car=strength_of_car, description=description,
                                  reg_date=datetime.utcnow())
    db.add(new_car, new_detail_car)
    db.commit()
    return True


def get_all_cars():
    db = next(get_db())
    cars = db.query(Cars).all()
    return cars


# def add_car_db(id, model_of_car, type, category_id, colour, id_detail strength_of_car, date_of_issue, amount_of_cars, description):
#     db = next(get_db())
#         new_car = Car(id=id, model_of_car=model_of_car, type=type, category_id=category_id, datetime=datetime.utcnow())
#         new_category = CategoryCar(id=category_id, colour=colour, strength_of_car=strength_of_car, id_detail=id_detail
#                       date_of_issue=date_of_issue, amount_of_cars=amount_of_cars, description=description, datetime=datetime.utcnow())
#         db.add(new_car)
#         db.add(new_category)
#         db.commit()
#         return "Successfully added"
