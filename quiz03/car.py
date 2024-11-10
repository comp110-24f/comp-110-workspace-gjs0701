class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, make: str, model: str, year: int, color: str, mileage: float):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def update_mileage(self, miles: float) -> None:
        self.mileage = miles

    def display_info(self) -> None:
        print(f"{self.make}, {self.model}, {self.year}, {self.color}, {self.mileage}")


def calculate_depreciation(my_car: Car, depreciation_rate: float) -> float:
    return my_car.mileage * depreciation_rate


my_ride: Car = Car("Honda", "CRV", 2015, "blue", 75000.00)
my_ride.update_mileage(5000.25)
my_ride.display_info()
print(calculate_depreciation(my_ride, 0.01))
