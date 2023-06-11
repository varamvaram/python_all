# f string using
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
#formating
print("My name is {} and I am {} years old.".format(name, age))
# Percentage formatting (% operator):
name1 = "Charlie"
age1 = 35
print("My name is %s and I am %d years old." % (name1, age1))

# Template Strings (string.Template):
from string import Template
name = "Dave"
age = 40
template = Template("My name is $name and I am $age years old.")
print(template.substitute(name=name, age=age))