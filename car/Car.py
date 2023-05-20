class Car:

    def __init__(self, car_type, acceleration, model, upgrade_array):
        assert isinstance(model, object)
        self.model = model
        self.acceleration = acceleration
        self.upgradeArray = upgrade_array
        self.car_type = car_type

    def print_car_status(self):
        print("\n-------------\nModel: ", self.model, "\nAcceleration: ", self.acceleration, "\nUpgrades: ",
              self.upgradeArray, "\n-------------\n")

    def calculate_distance(self,time):
        distance = 0
        distance += 0.5 * self.acceleration * time*time
        return distance
