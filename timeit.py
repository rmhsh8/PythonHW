import time

def calculate_time(func):
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        print('Total Time', y-x)
    return wrapper

def test():
    time.sleep(10)


test = calculate_time(test)
test()
