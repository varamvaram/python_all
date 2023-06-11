import mymodule
a = mymodule.person1["age"]
print(a)


import platform
person= platform.system()
print(person)
per1 = dir(platform)
print(per1)

from mymodule import person1

print (person1["age"])