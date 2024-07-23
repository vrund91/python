'''Takes user input,Calculates the length,Splits the string: 
If the length is greater than 15,
it attempts to split the string using a specified separator.'''

x=(input("Enter a string:"))
print(len(x))
if len(x) > 15:
	v=x.split(",",5)
print(v)