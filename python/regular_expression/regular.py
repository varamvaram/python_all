import re

txt = "The rain in Spain"
check = re.search("^The.*Spain$", txt)
if check:
  print("YES! We have a match!")
else:
  print("No match")

txt1 = "The rain in Spain"
check_detail = re.findall("ai", txt1)
print(check_detail)



txt2 = "The rain in Spain"
search_detail = re.search("\s", txt2)
print(search_detail.start())


split_detail= "space to separte key"
detail = re.split("\s", split_detail)
print(detail)
detail_sub= re.sub("\s", "9", txt)
print(detail_sub)

txt = "The Rain in Spain"
x = re.search(r"\bR\w+", txt)
print(x.group())
