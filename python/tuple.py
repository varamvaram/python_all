fruit = ("apple", "banana", "cherry")
print(fruit)

thistuple = (1, 3, 7, 4, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
index_value = thistuple.index(8)
print(index_value)

thistuple1 = ("apple", "banana", "cherry")
if "apple" in thistuple1:
  print("Yes, 'apple' is in the fruits tuple")

n_index= ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(n_index[-4:-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple_2 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple_2 += y
print(thistuple_2)

# unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

my_tuple = ('apple', 'banana', 'cherry', 'date')

# Loop through the elements in the tuple
for item in my_tuple:
    print(item)

while_1= ("apple", "banana", "cherry")
i = 0
while i < len(while_1):
  print(while_1[i])
  i = i + 1  

# join tuple
my_tuple = ('apple', 'banana', 'cherry', 'date')
# Join the elements of the tuple into a single string
joined_string = "-".join(my_tuple)
print(joined_string)