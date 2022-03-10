import time
def calculate_time(func):
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        print('Time it takes to execute is:', y-x, 'seconds')
    return wrapper

def test():
    print('Hi, how are you?')
test = calculate_time(test)
test()


    
