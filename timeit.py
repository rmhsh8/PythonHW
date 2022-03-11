import time

def calculate_time(func):
    def wrapper():
        begin = time.time()
        func()
        end = time.time()
        print('Total time ', end - begin)
    return wrapper


def test():
    time.sleep(10)


test = calculate_time(test)
test()