#Day2
#program-4

x = int(input("number of pattern"))
z=x
y=x
for i in range(x):
    print("*" * z + "  " * (i+1) + "*" *z)
    z = z - 1
for j in range(x):
    print("*" * (j+1) + "  " * y + "*" * (j+1))
    y = y-1