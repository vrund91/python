'''string starting index from 0 to 1....'''
str1="hello world"
print("convert first character.",str1.capitalize())

str2="I love apples,apples is my favourite"
x=str2.count("apples",7,22)
print("The substring in string is:",x)

str3="This is string example.."
sub="i"
print(str3.count(sub,1,40))

str4="This is string example....wow!"
suffix="wow!"
print("check index using find string:",str4.endswith(suffix))
print("check index using find string:",str4.endswith(suffix,26,30))

str5="This is string example...."
str6="example"
str7="index"
print("This is return index beg & end:-",str5.find(str6))
print("This is return index beg & end:-",str5.find(str7))

str7="..."
print("This string is alphanumeric:",str7.isalnum())

str8="ty2024"
print("This string is alphanumeric:",str8.isalnum())

str9="table23"
str10="table"
print("All character are  alphabets:" ,str9.isalpha())
print("All character are alphabets:" ,str10.isalpha())

str11="23456"
print("This string is Digit:",str11.isdigit())

str12="this is string example"
str13="This is string example"
print("This string is a LowerCase:" ,str12.islower())
print("This string is a LowerCase:" ,str13.islower())

str14="This is string example"
str15="THIS IS STRING EXAMPLE"
print("This string is a UpperCase:",str14.isupper())
print("This string is a UpperCase:",str15.isupper())

str16=" "
str17="ABC"
print("check whitespace character:",str16.isspace())
print("check whitespace character:",str17.isspace())

str18="ABC"
print("Return length of Object:",len(str18))

str20="THIS IS STRING EXAMPLE"
print("convert into LowerCase:",str20.lower());

str21="this is string example"
print("convert into UpperCase:",str21.upper());

str22="HELLO PYTHON"
print("check string starts with H:",str22.startswith("H"))
print("check string starts with beg to end:",str22.startswith(str22,0,13))

str23="Welcome to python"
print("swap character to upper to lower:",str23.swapcase())

str24="  Welcome to 2024  "
print("Removes Both Leading and Trailing character",str24.lstrip())

str25="@@@@ Welcome to mscit @@@@"
print("Removes Leading character",str25.lstrip('@'))

str26="@@@@ Welcome to mscit @@@@"
print("Removes Trailing character",str26.rstrip('@'))