def add(*args):
    print(sum(args))

add(1,2,3,4,5)

def calculate(n, **kwargs):
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    return n


print(calculate(2, add=2, multiply=3))

