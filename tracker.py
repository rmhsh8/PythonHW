def func_counter(func):
    def wrapper(*args,**kw):
        result = func()
        wrapper.counter += 1
        print(f'Number of times executed: {wrapper.counter}')
        return result
    wrapper.counter = 0
    return wrapper


@func_counter
def foo():
    print("Hello, World!")
foo()
foo()
