# using *args in functions

def add(*args):
    for number in args:
        sum_of_numbers = sum(args)
        print(sum_of_numbers)


add(5, 5, 5)


# using **kwargs in functions
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 3, multiply = 5)


#using **kwargs in class init

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # using get function helps if user doesn't specify a keyword, but calls for it
        self.model = kw.get("model")

my_car = Car(make = "Nissan", model = "GT-R")

print(my_car.model)