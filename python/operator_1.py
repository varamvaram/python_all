print(not 5 == 5)
print(1 or 2 and 3)
first= 5
second = 3
print(first == second)
print(first != second)
print(first>second)
print(first<second)
print(first>=second)
print(first<=second)
grater=5
print(grater > 3 and grater < 10)
print(grater > 3 or grater < 10)
print(not grater > 3 and grater < 10)

fruit1= ["apple", "banana"]
fruit2= ["apple", "banana"]
fruit3= fruit1

print(fruit1 is fruit3)

# returns True because z is the same object as x

print(fruit1 is not fruit2)

# returns False because x is not the same object as y, even if they have the same content

print(fruit1 == fruit2)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y