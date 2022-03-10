import time
def calculate_time(func):
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        print('Total Time', y-x, 'seconds')
    return wrapper

def test():
    time.sleep(5)
test = calculate_time(test)
test()
