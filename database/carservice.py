from database.models import Cars, CategoryCars
from database import get_db


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


def change_car_db(id, change_info, new_data):
    db = next(get_db())
    car = db.query(Cars).filter_by(id=id).first()
    if car:
        if change_info == 'model':
            car.model_of_car = new_data
        elif change_info == "type":
            car.type_of_car = new_data
        else:
            return "This type not found"
        db.commit()
        return "Successfully changed!"
    return "Car not found"


def add_car_db(id, model_of_car, type_of_car, category_id):
    db = next(get_db())
    new_car = Cars(id=id, model_of_car=model_of_car, type_of_car=type_of_car, category_id=category_id)
    if new_car:
        db.add(new_car)
        db.commit()
        return "Car successfully added"
    else:
        return False


def add_car_detail_db(id_detail, strength_of_car, date_of_issue, amount_of_cars, description, colour):
    db = next(get_db())
    new_detail_car = CategoryCars(id_detail=id_detail, amount_of_cars=amount_of_cars, date_of_issue=date_of_issue, colour=colour,
                                  strength_of_car=strength_of_car, description=description)
    if new_detail_car:
        db.add(new_detail_car)
        db.commit()
        return "Car successfully added"
    else:
        return False


def get_all_cars():
    db = next(get_db())
    cars = db.query(Cars).all()
    return cars
