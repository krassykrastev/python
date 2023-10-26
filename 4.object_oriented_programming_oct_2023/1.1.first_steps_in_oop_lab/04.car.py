# Create a class called Car. Upon initialization, it should receive a name, model, and engine (all strings).
# Create a method called get_info() which will return a string in the following format:
# "This is {name} {model} with engine {engine}".
#
# Example:
# car = Car("Kia", "Rio", "1.3L B3 I4")
# print(car.get_info())
#
# Output:
# This is Kia Rio with engine 1.3L B3 I4

class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())
