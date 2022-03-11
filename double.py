def doubler(func):
    def math():
        func()
        func()
    return math
    
@doubler
def solve():
    print("Hello, World")
solve()