#To check whether a string starts with specified characters.

str=input("Enter a string : ")
comp=['A','E','I','O','U','a','e','i','o','u']
#if str[0]=='a' or str[0]=='A' :
if str[0] in comp :
    print(str, "is starting with vowel")
else:
    print(str, "is not starting with vowel")