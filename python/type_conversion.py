num_str = "10"
num_int = int(num_str)
print(num_int)  # Output: 10
num_1= "3.14"
num_float = float(num_1)
print(num_float)  # Output: 3.14

num = 10
num_2 = str(num)
print(num_2)  # Output: "10"

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

my_list1 = [1, 2, 3]
my_tuple = tuple(my_list1)
print(my_tuple)  # Output: (1, 2, 3)

my_list2 = [1, 2, 3, 2, 1]
my_set = set(my_list2)
print(my_set)  # Output: {1, 2, 3}

my_list3 = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(my_list3)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}