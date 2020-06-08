#day 3
#program - 4

n1= input("Enter numbers followed by a space for list-1")
n1 = n1.strip()
list_1 = n1.split(" ")
n2 = input("Enter numbers followed by a space for list-2")
n2 = n2.strip()
list_2 = n2.split(" ")
list_3 = []
z = 0

print("The intersection of the two python lists are: ")
for i in range(0,len(list_1)):
    for j in range(0,len(list_2)):
        if list_1[i] == list_2[j]:
            list_3.append(list_2[j])
            if i != len(list_1)-1:
                print(list_3[z],end=",")
                z += 1
            else:
                print(list_3[z])