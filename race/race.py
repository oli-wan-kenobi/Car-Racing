import random
from time import sleep

from car.Car import Car


def race(car):
    model = ["Nissan Skyline", "Ford GT", "Toyota Corolla"]
    opponent = Car(0, random.randint(1, 7), random.choice(model), [0, 0, 0, 0, 0])
    print("This is your opponent!")
    opponent.print_car_status()

    distance1 = 0
    distance2 = 0
    time = 0
    points = 0
    while distance1 < 400 and distance2 < 400:
        distance1 = car.calculate_distance(time)
        distance2 = opponent.calculate_distance(time)
        print("Your distance: %.2f" % distance1, "\nOpponents distance: %.2f" % distance2)
        position1 = int(distance1 / 8)
        position2 = int(distance2 / 8)
        for i in range(0, 70):
            if i != position1 and i != 50:
                print("-", end="")
            elif i == 50:
                print("|", end="")
            else:
                print("🚗", end="")
        print("")
        for j in range(0, 70):
            print(".", end="")
        print("")
        for k in range(0, 70):
            if k != position2 and k != 50:
                print("-", end="")
            elif k == 50:
                print("|", end="")
            else:
                print("🚓", end="")
        print("")

        modulo = distance1 % 100
        if distance1 >= 100 and modulo < 50:
            points += 5
        time += 1
        sleep(0.2)

    if distance1 > distance2:
        print("You win")
        points += 20
    elif distance2 > distance1:
        print("Opponent wins")
    else:
        print("it's a tie")
        points += 10
    return points
