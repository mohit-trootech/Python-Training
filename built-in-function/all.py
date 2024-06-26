"""
all: All functions in python replace the loops by returning true for all values
Except: empty string, False, 0
"""

print(all([1, 2, 3, 4]))
print(all([1, 2, 3, 0]))
print(all([1, 2, '', 3]))
print(all([1, '', 3]))


# Example to check if a car is ok
def is_car_ok(car_tyres, car_color, car_mileage):
    return all([car_mileage, car_tyres, car_color])


is_car_ok(4, 'blue', '45hp')
is_car_ok(0, 'blue', '45hp')
is_car_ok(4, '', '45hp')
is_car_ok(4, 'black', '0')


# check it ingredients available
class Cook:

    def __init__(self, tomato, potato, paneer):
        self.tomato = tomato
        self.potato = potato
        self.paneer = paneer

    def cook_panner(self, tomato, paneer):
        self.tomato -= tomato
        self.paneer -= paneer
        if all([self.tomato, self.paneer]):
            print("Cook Panner")
        else:
            print("Unavailable Ingredients For Paneer")

    def cook_potato(self, tomato, potato):
        self.tomato -= tomato
        self.potato -= potato
        if all([self.tomato, self.potato]):
            print("Cook Potato")
        else:
            print("Unavailable Ingredients For Potato")


cooking = Cook(10, 10, 10)
cooking.cook_panner(5, 5)
cooking.cook_potato(5, 5)


