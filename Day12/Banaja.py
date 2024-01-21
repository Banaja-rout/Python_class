def square(limit):
    for i in range(1,limit):
        yield i ** 2
       
square_gen = square(5)
for s in square_gen:
    print(s)
