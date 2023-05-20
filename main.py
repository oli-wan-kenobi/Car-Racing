from gameplay.play_round import play_round
from initialization import choose_car

if __name__ == '__main__':
    car = choose_car.select()
    print("Great! This is your car!")
    car.print_car_status()
    play_round(car)
