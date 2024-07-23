''' Write a Python program to remove duplicates from a list.'''
user_input=(input("Enter a string:"))
element = user_input.split()
unique_element = list(set(element))
print("unique element:",unique_element)


