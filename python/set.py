fruits = {"apple", "banana", "cherry"}
fruits_1={"google","microsoft",}
fruits.add("orange")
print(fruits)
# fruits.clear()
#print(fruits)
frit_1= fruits.copy()
print(frit_1)
fruits.pop()
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.update(fruits_1)
print(fruits)
# loop
for x in fruits:
    print(x)