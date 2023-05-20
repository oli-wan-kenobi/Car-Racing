from car.Car import Car


def select():
    print("Welcome to Python Drag Racing!")
    print("Please select your car and difficulty from the list!\n")
    car_type = int(input("0: Bugatti Veyron (Easy)\n1: Ford Mustang (Medium)\n2: Toyota Yaris (Hard)\n"))

    if car_type == 0:
        car = Car(0, 3, "Bugatti Veyron", [0, 0, 0, 0, 0])
        return car
    elif car_type == 1:
        car = Car(0, 2, "Ford Mustang", [0, 0, 0, 0, 0])
        return car
    elif car_type == 2:
        car = Car(0, 1, "Toyota Yaris", [0, 0, 0, 0, 0])
        return car
    else:
        print("error")
        select()
