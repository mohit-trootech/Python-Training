class Person:
    def method(self):
        pass


p_obj = Person()
p_obj.name = "Mohan"
print(p_obj.name)
# p_obj.method.whoami = "I am Mohit"
p_obj.method.__func__.whoami = f'i am {p_obj.name}'
print(p_obj.method.whoami)

p_obj = Person()
p_obj.name = "Trever"
print(p_obj.name)
# p_obj.method.whoami = "I am Mohit"
p_obj.method.__func__.whoami = f'i am {p_obj.name}'
print(p_obj.method.whoami)
