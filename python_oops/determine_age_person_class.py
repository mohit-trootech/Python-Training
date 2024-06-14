import datetime
from check_number_input import is_number


class Person:
    now = datetime.date.today()

    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country

    def get_age(self):
        age_now = Person.now - self.dob
        age_now = age_now // datetime.timedelta(weeks=52)
        return "{} is Now {} Years Old".format(self.name, age_now)


n = input("Enter Your Name: ")
c = input("Enter the Country: ")
print("Enter Your Date of Birth: ")
y = input("Enter the Date of Year: ")
m = input("Enter the Date of Month 1-12: ")
d = input("Enter the Date of Day 1-31: ")
person_obj = Person(n, datetime.date(int(y), int(m), int(d)), c)

print(person_obj.get_age())