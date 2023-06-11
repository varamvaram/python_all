my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

#my_list.clear()
#print(my_list)

new_list = my_list.copy()
print(new_list)

count = my_list.count(2)
print(count) 

my_list1 = [1, 2, 3]
another_list = [4, 5]
my_list1.extend(another_list)
print(my_list1)

my_list2 = [1, 2, 3]
my_list2.insert(1, 5)
print(my_list2) 

my_list3 = [1, 2, 3]
removed_item = my_list3.pop(1)
print(removed_item)  # Output: 2
print(my_list3)  # Output: [1, 3]

my_list4 = [1, 2, 3, 2]
my_list4.remove(2)
print(my_list4)  # Output: [1, 3,2]

my_list5 = [1, 2, 3]
my_list5.reverse()
print(my_list5)  # Output: [3, 2, 1]

my_list6 = [3, 1, 2]
my_list6.sort()
print(my_list6)  # Output: [1, 2, 3]