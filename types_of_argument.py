# Python Program to Describe Different Type of Arguments
print("Default Variable")
def dv(name="Mohit", age=23):
    print("User Name {} and {}".format(name,age))
dv()
dv("Yash",25)

print("Position Arguments")
def pa(name,age,city):
    print("User Name is {}, Age is {}, Lives in {}".format(name,age,city))

pa("Mohit",23,"Aburoad")
pa("Aburoad",23,"Mohit")

print("Variable Length Arguments - *args")

def myfunc1(*args):
    for i in args:
        print(i)
myfunc1("Mohit","Yash","Mohan","Veena")

print("Keyword Variable Length Arguments - **kwargs")

def myfunc2(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
myfunc2(Name="Mohit",age=26,city="Ahmedabad")
myfunc2(Name="Naman",age=24,city="Mumbai")
