''' Write a program to accept a string from the user and display characters that are 
present at an even index number.'''

x=(input("Enter a string:"))
result_string=""
for index in range(len(x)):
    if index % 2 == 0:
        result_string += x[index]
        print("Even character is:",result_string)