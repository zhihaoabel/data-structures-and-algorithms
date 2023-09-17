def prod(a, b):
    return a * b


def fact_gen():
    i = 1
    n = 1

    while True:
        yield prod(i, n)
        n = prod(i, n)
        i += 1


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))