import time

def decor(fn):
    def wrapper(*args, **kwargs):

        start = time.time()
        res = fn()
        print( "Время выполнения программы:", time.time() - start)

        return res
    return wrapper

@decor
def func():
    for i in range(1,1_000_000_000):pass

func()
