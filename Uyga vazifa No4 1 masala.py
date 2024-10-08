import csv
from abc import ABC, abstractmethod

# 1-masala
class Vehicle(ABC):
    def __init__(self, model, brand, year, mileage):
        self.__mileage = mileage
        self.__year = year
        self.__brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, new_mileage):
        self.__mileage = new_mileage

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def write_csv(self):
        with open("Vehicle.csv", mode="a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.brand, self.model, self.year, self.mileage])

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}, Mileage: {self.mileage} km"


class Car(Vehicle):
    def __init__(self, model, brand, year, mileage, num_doors):
        super().__init__(model, brand, year, mileage)
        self.__num_doors = num_doors

    def start(self):
        return f"{self.brand} {self.model} is starting with a roar!"

    def stop(self):
        return f"{self.brand} {self.model} has stopped."

    def open_trunk(self):
        return f"The trunk of the {self.brand} {self.model} is now open."

class Bicycle(Vehicle):
    def __init__(self, model, brand, year, mileage, gear_count):
        super().__init__(model, brand, year, mileage)
        self.__gear_count = gear_count

    def start(self):
        return f"{self.brand} {self.model} is starting quietly."

    def stop(self):
        return f"{self.brand} {self.model} has stopped."

    def ring_bell(self):
        return "Ring ring! The bell is ringing."

car = Car("Camry", "Toyota", 2020, 15000, 4)
bicycle = Bicycle("Escape 3", "Giant", 2022, 500, 21)

car.write_csv()
bicycle.write_csv()

print(car.get_info())
print(car.start())
print(car.open_trunk())
print(car.stop())

print()

print(bicycle.get_info())
print(bicycle.start())
print(bicycle.ring_bell())
print(bicycle.stop())



