# Remove a key from a dictionary?

dict1 = {"C programming" : ".c",
         "C plus plus" : ".cpp-mistyped",
         "Python" : ".py",
         "one" : 1,
         "two":2
         }

print("items in dictionary before deletion :", dict1)
print("Enter key to be deleted")
key_del=input()
for w in dict1:
    if w==key_del:
        del dict1[w]
        break
print("items in dictionary after deletion operation:", dict1)
