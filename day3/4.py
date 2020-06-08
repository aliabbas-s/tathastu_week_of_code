#Day-3
#program - 4

list_original = []
n = (input("Enter numbers followed by a space"))
n = n.strip()
list_copy=[]
list_original = (n.split(" "))
print("Your list is : ",list_original)

for i in range(0,len(list_original)):
    if list_original[i] not in list_copy:
        list_copy.append(list_original[i])
print("The List without duplicates is : ",list_copy)