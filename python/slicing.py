text = "Hello, World!"
# Slicing
slice_1 = text[7:12]  # Extracts characters from index 7 to 11 (inclusive)
slice_2 = text[:5]  # Extracts characters from the start up to index 4
slice_3 = text[7:]  # Extracts characters from index 7 to the end
slice_4 = text[::2]  # Extracts every second character
slice_5 = text[::-1]  # Reverses the string

# Printing the slices
print("Slice 1:", slice_1)  # Output: World
print("Slice 2:", slice_2)  # Output: Hello
print("Slice 3:", slice_3)  # Output: World!
print("Slice 4:", slice_4)  # Output: HloWrd
print("Slice 5:", slice_5)  # Output: !dlroW ,olleHa = "Hello, World!"

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("H", "J"))
print(text.split(",")) 

tex1="hello"
tex2="world"
text = tex1+ " " + tex2
print(text)

age=26
concatinate="hello world {}"
print(concatinate.format(age))

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

txt1 = 'It\'s alright.'
print(txt1)

txt2 = "This will insert one \\ (backslash)."
print(txt2) 

txt3 = "Hello, welcome to my world."
x = txt3.find("e")
print(x)