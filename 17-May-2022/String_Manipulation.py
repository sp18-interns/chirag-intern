# This example will demonstrate how you can do several things with strings.
#
# 1. Convert a string to Lower Case.
# 2. Convert a string to Upper Case
# 3. Capitalize a String
# 4. Slice substrings from a string
# 5. Find a particular substring in a string
# 6. Chop of leading and trailing characters from strings.
# 7. Find out the length of strings
# 8. Replace a substring by another.


testString1 = "Hello World!"
print("Original String: "+ testString1)
print("-"*50)
print("Converting to Upper Case")
print(testString1.upper())
print("-"*50)
print("Capitalizing the String")
print(testString1.capitalize())
print("-"*50)
print("Substring from index 1 to 7")
print(testString1[1:8])
print("-"*50)
print("Find the index from which the substring 'llo' begins within the test string")
print(testString1.find('llo'))
print("-"*50)
print("rfind('l') on the given string returns the following index (this scans the string from right to left):")
print(testString1.rfind('l'))