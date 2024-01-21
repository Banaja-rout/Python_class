# ***********MAP*********

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperatures_c = [10, 15, 20, 30, 50]

temperatures_f = map(celsius_to_fahrenheit, temperatures_c)

print(temperatures_f)


# ***********FILTER*********

def is_negative(num):
    return num < 0

num = [5,-9,-6,25,-56,-3,8,98,-65]

negative_nums = filter(is_negative, num)

print(list(negative_nums))


# ***********REDUCE*********

from functools import reduce

def concatenate(a, b):
    return a + " " + b

str = ["Good", "Afternoon", "Everyone"]

result = reduce(concatenate, str)
print(result)

