"""
abs: Absolute function: return the absolute values of integers & floating point numbers
takes int|float|complex number as parameter & Return its absolute value, irrespective of sign always return positive value
in the case of complex number return magnitude by formula - sqrt(x**2+y**2)
in case of list use map function & in case of str: return error
"""
a = 1
b = -1
c = 2
d = 1 + 2j
# e = 'hi'
f = [1, -1, 2.2, -2.2, 2 + 2j, -2 + 2j, 2 - 2j]

print(type(a), abs(a))
print(type(b), abs(b))
print(type(c), abs(c))
print(type(d), abs(d))
# print(type(e), abs(e)) #return error since e:str
print(type(f), list(map(abs, f)))  #use a map for list


def distance_travel(speed, time):
    print(f"Car Speed: {speed}")
    print(f"Time Taken: {time}")
    return f"Distance travel by Car: {speed*time}"


def car_speed(distance, time):
    print(f"Distance Travelled: {distance}")
    print(f"Time TakenTravelled: {time}")
    return f"Car Speed: {distance/time}"


def time_taken(speed, distance):
    print(f"Car Speed: {speed}")
    print(f"Distance Travelled: {distance}")
    return f"Time Taken by Car: {distance/speed}"


print(car_speed(abs(54.5), abs(2.5)))
print(distance_travel(abs(-10), abs(2.5)))
print(time_taken(abs(-5), abs(-5)))

