# Assignment 1: Design Your Own Class! 🏗️
# Smartphone Class
class Smartphone:              
    def __init__(self, brand, model, storage, color, is_on, photo_size, number):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        self.is_on = False
        self.photo_size = "1MB"
        self.number = number


    def smartphone_details(self):
        print(f"My phone is a {self.brand} {self.model}  {self.storage}  {self.color} { self.is_on}  {self.photo_size}  {self.number} and I love it!")


    def make_call(self):
        if self.is_on:
            print(f"Calling {self.number} from {self.brand} {self.model}...")
        else:
            print("This phone cannot make calls.")

    def take_photo(self):
        if self.is_on:
            print(f"Capturing a photo with {self.brand} {self.model}...")
        else:
            print(f"Cannot take a photo. {self.brand} {self.model} is off.")


my_phone = Smartphone("Xiaomi", "Redmi Note 10", "128GB", "Black", "is_on", "1MB", "+245708679439")
my_phone.smartphone_details()


my_phone = Smartphone("Xiaomi", "Redmi Note 10", "128GB", "Black", False, "1MB", "+245708679439")
my_phone.is_on = True  # Turn the phone on to make a call
my_phone.make_call()


my_phone = Smartphone("Xiaomi", "Redmi Note 10", "128GB", "Black", False, "1MB", "+245708679439")
my_phone.is_on = True  # Turn the phone on to take a photo
my_phone.take_photo()


# Activity 2: Polymorphism Challenge! 🎭
# Polymorphism with Vehicles 🚗✈️🚢
class vehicle:
    def move(self):
        print("The vehicle is moving")

class car(vehicle):
    def move(self):
        print("The car is Driving")

class plane(vehicle):
    def move(self):
        print("The plane is Flying")

class boat(vehicle):
    def move(self):
        print("The boat is Sailing")

class train(vehicle):
    def move(self):
        print("The train is Chugging")

for v in (car(), plane(), boat(), train()):
    v.move()
    # print(v.move())

