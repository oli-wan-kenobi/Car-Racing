from car.Car import Car


def upgrade(points, car):
    print("Your points are: ", points)
    print("Choose an upgrade: ")
    price = [100, 100, 100, 100, 100]
    for i in car.upgradeArray:
        if i > 0:
            price[i] += price[i] * i
    print("Available upgrades: \n0:Intake\t\t\t", car.upgradeArray[0], "\tPrice : ", price[0],
          "\n1:Exhaust\t\t\t", car.upgradeArray[0], "\tPrice : ", price[1],
          "\n2:Transmission\t\t", car.upgradeArray[2], "\tPrice : ", price[2],
          "\n3:Weight Reduction\t", car.upgradeArray[3], "\tPrice : ", price[3],
          "\n4:Tires\t\t\t\t", car.upgradeArray[4], "\tPrice : ", price[4], "\n5:Exit ")

    component_upgrade = int(input("Which one you want to upgrade? "))
    if component_upgrade == 5:
        return points
    if points >= price[component_upgrade]:
        car.upgradeArray[component_upgrade] += 1
        points -= price[component_upgrade]
        car.acceleration += 0.2
        print("Purchase successful")
        return points
    else:
        print("Insufficient funds")
        return points
