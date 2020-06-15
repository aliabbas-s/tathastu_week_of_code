#day 4
#program -1

list_one = input("Enter elements seperated by a space for a tuple")
tuple_one = tuple(list_one.strip().split(" "))

count = 0
list_two = []
for i in range(0,len(tuple_one)):
    if tuple_one[i] not in list_two:
        for j in range(0,len(tuple_one)):
            if tuple_one[i] == tuple_one[j]:
                list_two.append(tuple_one[i])
                count += 1

        print(tuple_one[i], " occurs ", count, " times")
        count = 0





