def func(start, step):
    current = start
    while True:
        yield current
        current += step

generator = func(1, 2)

for i in range(10):
    print(next(generator))
