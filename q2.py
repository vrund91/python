'''write a Python program to count the number of strings from a given list of strings. 
The string length is 2 or more and the first and last characters are the same.
 Sample List : ['abc', 'xyz', 'aba', '1221']'''

str_list=['abc','xyz','aba','1221']
count=0

for s in str_list:
    if len(s) >= 2 and s[0]==s[-1]:
        count +=1
        print("Number of string with same first and last character:",count)
