from prime_number_module import prime_number_check

print("""
Program to Find Sum of all the Prime Numbers from  1 to 2000 [Prime Number Module is Imported] 
""")

prime_sum = 0

for i in range(1,2000):
    if prime_number_check(i):
        prime_sum = prime_sum+i

print("Sum to 2000 Prime Number {}".format(prime_sum))


