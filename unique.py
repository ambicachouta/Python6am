# 1. That accepts a comma separated sequence of words as input
# and prints the unique words in sorted form (alphanumerically).


s=int(input("Enter the size of the list :"))
words=[0]*s
for i in range(s):
    print("Enter word %d :" %(i+1))
    words[i]=input()
print ("the words sre : ",words)
print("The unique list of words :")
unique=[]
for w in words:
    if w not in unique:
        unique.append(w)
print(unique)
unique.sort()
print("The sorted unique list is : ",unique)
print("End of program")


