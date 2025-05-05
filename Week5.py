# Assignment 1: Design Your Own Class! 🏗️
# Smartphone Class
class Smartphone:  # Define a class named Smartphone
    def __init__(self, brand, model, storage, color, is_on, photo_size, number):
        # Initialize the attributes of the Smartphone class
        self.brand = brand  # Brand of the smartphone
        self.model = model  # Model of the smartphone
        self.storage = storage  # Storage capacity of the smartphone
        self.color = color  # Color of the smartphone
        self.is_on = False  # Boolean to indicate if the phone is on (default is False)
        self.photo_size = "1MB"  # Default photo size
        self.number = number  # Phone number associated with the smartphone

    def smartphone_details(self):  # Method to display smartphone details
        print(f"My phone is a {self.brand} {self.model}  {self.storage}  {self.color} {self.is_on}  {self.photo_size}  {self.number} and I love it!")

    def make_call(self):  # Method to make a call
        if self.is_on:  # Check if the phone is on
            print(f"Calling {self.number} from {self.brand} {self.model}...")
        else:
            print("This phone cannot make calls.")  # Print message if the phone is off

    def take_photo(self):  # Method to take a photo
        if self.is_on:  # Check if the phone is on
            print(f"Capturing a photo with {self.brand} {self.model}...")
        else:
            print(f"Cannot take a photo. {self.brand} {self.model} is off.")  # Print message if the phone is off


# Create an instance of the Smartphone class and display its details
my_phone = Smartphone("Xiaomi", "Redmi Note 10", "128GB", "Black", "is_on", "1MB", "+245708679439")
my_phone.smartphone_details()

# Create another instance of the Smartphone class and make a call
my_phone = Smartphone("Xiaomi", "Redmi Note 10", "128GB", "Black", False, "1MB", "+245708679439")
my_phone.is_on = True  # Turn the phone on to make a call
my_phone.make_call()

# Create another instance of the Smartphone class and take a photo
my_phone = Smartphone("Xiaomi", "Redmi Note 10", "128GB", "Black", False, "1MB", "+245708679439")
my_phone.is_on = True  # Turn the phone on to take a photo
my_phone.take_photo()

# Activity 2: Polymorphism Challenge! 🎭
# Polymorphism with Vehicles 🚗✈️🚢
class vehicle:  # Define a base class named vehicle
    def move(self):  # Base method to describe movement
        print("The vehicle is moving")

class car(vehicle):  # Define a subclass car that inherits from vehicle
    def move(self):  # Override the move method
        print("The car is Driving")

class plane(vehicle):  # Define a subclass plane that inherits from vehicle
    def move(self):  # Override the move method
        print("The plane is Flying")

class boat(vehicle):  # Define a subclass boat that inherits from vehicle
    def move(self):  # Override the move method
        print("The boat is Sailing")

class train(vehicle):  # Define a subclass train that inherits from vehicle
    def move(self):  # Override the move method
        print("The train is Chugging")

# Demonstrate polymorphism by iterating through different vehicle types
for v in (car(), plane(), boat(), train()):  # Create instances of each subclass
    v.move()  # Call the move method for each instance
    # print(v.move())  # (Commented out) Print the result of calling move

