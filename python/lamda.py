single = lambda a : a + 10
print(single(5))
multiple = lambda a, b, c : a + b + c
print(multiple(5, 6, 2))


def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))
