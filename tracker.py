def doubler(func):
    def math():
        x = func()
        return x ** 3
    return math
def dec(func):
    def math():
        x = func()
        return x // 2
    return math
    
@doubler
@dec
def solve():
    x = 9
    return x
print(solve())