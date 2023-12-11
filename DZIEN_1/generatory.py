#przykład 1

def liczby():
    for i in range(17):
        yield i*2

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)


#przykład 2
def wznowienia(n,k):
    print("wstrzymanie działania 0")
    yield 1005
    print("wznowienie działania 1")

    print("wstrzymanie działania 0")
    yield n+k
    print("wznowienie działania 1")

    n = 8*k-2

    print("wstrzymanie działania 0")
    yield n-k
    print("wznowienie działania 1")

    print("wstrzymanie działania 0")
    yield n*k
    print("wznowienie działania 1")

    print("wstrzymanie działania 0")
    yield n**k
    print("wznowienie działania 1")

print(wznowienia(6,8))
print(tuple(wznowienia(6,8)))

print("_"*50)
for i in wznowienia(6,8):
    print("_"*35)
    print(type(i))
    print(f'zwrócono wartość: {i}')
print("_"*50)
