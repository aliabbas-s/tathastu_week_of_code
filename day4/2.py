#Day 4
#Program 2
from operator import itemgetter
number = int(input("how many lists you want in a tuple?"))
original_tuple = []
list_copy =[]
x_2 = []
for i in range(0,number):
    x_1 = int(input("enter size of list within tuple"))
    for i in range (0,x_1):
        x_2.append(int(input("Enter elements")))
    original_tuple.append(tuple(x_2))
    x_2 = []
print(original_tuple)

N = 1
original_tuple.sort(key = itemgetter(N) )
print("List after sorting tuple by Nth index sort : " + str(original_tuple))