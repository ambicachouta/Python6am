# Get the maximum and minimum value in a dictionary.

dict1={"DBMS":80, "DS with Python":55,"Software Engineering":90}
print(dict1)
list=[]
for k,v in dict1.items() :
    list.append(v)
    list.sort()

print(list)
print("maximum value in the dictionary = ",list[0])
print("minimum value in the dictionary = ",list[-1])

"""str=min(dict1)
print(str)
for w in dict1 :
    if w==str:
        print("minimum value in the dictionary = ",dict1[w])
        break
"""

#doubts

# Get the last part of a string before a specified character
# Sort a list alphabetically in a dictionary
# Generate and print a dictionary that contains a number (between 1 and n) in the form (a, a*a).

