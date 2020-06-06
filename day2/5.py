# Day -2
#Program 5

num = int(input("Enter number"))

for i in range(num,0,-1):
    for j in range(i):
        if j == i-1:
            print(i)
        else:
            print(i,end="*")
for i in range(num+1):
    for j in range(i):
        if j == i-1:
            print(i)
        else:
            print(i,end="*")