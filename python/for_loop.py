for num in range(1, 11):
    if num % 2 == 0:
        continue
    if num == 9:
        break
    print(num)

def my_detail(fname):
  print(fname + " Refsnes")

my_detail("Emil")
my_detail("Tobias")
my_detail("Linus")