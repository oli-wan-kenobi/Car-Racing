import car
from race.race import race
from upgrade.upgrade import upgrade


def play_round(race_car):
    points = 0
    selection = 0
    while selection != 2:
        print("What do you want to do this round?")
        selection = int(input("0: Race\n1: Upgrade car\n2: Exit\n"))
        if selection == 0:
            points += race(race_car)
            print("Total points: ", points, "\n\n")
        if selection == 1:
            points = upgrade(points, race_car)
