import time
def calculate_time(func):
    def wrapper():
        x = func()
        input()
        y = func()
        print('Total Time', y-x, 'seconds')
    return wrapper

def test():
    return time.time()


test = calculate_time(test)
test()