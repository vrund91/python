'''Write a Python program to find the list of words that are longer than n from a given
 list of words'''
string=(input("Enter a your string:"))
a=string.split()
b=[]
n=int(input("Enter your n:"))
for i in a:
    if len(i) > n :
        b.append(i)
        print("lsit is of i than {n} Character:",b)