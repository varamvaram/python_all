global_var = "awesome"

def myfunc():
  print("Python is " + global_var)

myfunc()
x="tree looking nice"
def myfunc():
  global xs
  x = "fantastic"

myfunc()

print("Python is " + x)