#fruits = ["apple", "banana", "cherry"]
fruits="apple"
# Create an iterator from the iterable
fruits_iter = iter(fruits)

# Iterate over the elements using the iterator
print(next(fruits_iter))  # apple
print(next(fruits_iter))  # banana
print(next(fruits_iter))  # cherry

# Using a for loop to iterate over the iterable directly
for fruit in fruits:
    print(fruit)