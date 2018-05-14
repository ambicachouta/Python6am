#Lowercase first n characters in a string.

str=input("Enter a string : ")
number=int(input("Enter the number of lowercase characters to be displayed : "))
count=0
lc=[]
for a in str:
    if ord(a)>=97 and ord(a)<=122 :
        lc.append(a)
        count=count+1
    if count==number:
        break
print(lc)


