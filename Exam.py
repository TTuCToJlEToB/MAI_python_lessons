from time import *
def dec(func):
    def wrapp():
        start = time()
        a = func()
        print( "Done in:", time() - start)
        return a
    return wrapp

@dec
def func():
    print("Start")
    for i in range(1,1_000_000_000):pass

func()