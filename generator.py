def squres(n):
    for i in range(1,n+1):
        yield i*i

x=squres(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))