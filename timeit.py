import time
def calculate_time(func):
    def wrapper(*args, **kw):
        x = time.time()
        result = func(*args, **kw)
        y = time.time()
        print(f'Total Time', int(y-x), 'seconds')
        return result
    return wrapper

@calculate_time
def test():
    for i in range (int(10e7)):
        pass

test()
