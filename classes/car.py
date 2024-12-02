#attributes: has_heated_steering, price, model, odometer

class Person:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        

class Car:

    def __init__(self, has_heated_steering: bool, price: float, model: str, odometer: float, owner: Person) -> None:
        self.has_heated_steering = has_heated_steering
        self.price = price
        self.model = model
        self.odo = odometer
        self.owner = owner

    def drive(self, distance: float) -> None:
        self.odo += distance
    
    def __str__(self) -> str:
        return f'{self.model} with {self.odo}km'


eric = Person('Eric', 'echalmers@mtroyal.ca')

fleet = [
    Car(False, 500, "GMC Sierra", 150_000, eric),
    Car(True, 100000000, "Porche Cayenne", 3, eric),
    Car(False, 10_000, "Ford Prefect", 25000, eric),
]

# search through the list and print out all 
# cars with < 100,000 km
for car in fleet:
    if car.odo < 100_000:
        print(car, car.owner.email)


# get the first car from the fleet and drive it 1000 km
rented_car = fleet[0]
print(f'cars current odometer: {rented_car.odo}')
rented_car.drive(1000)
print(f'cars current odometer: {rented_car.odo}')
