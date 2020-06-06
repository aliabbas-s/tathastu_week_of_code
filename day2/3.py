#Day-2
#Program-3

pattern = int(input("Enter number for cross pattern"))
for i in range(pattern):
    print(" " * i + "*" + "  " *(pattern-1-i)+ "*")
for i in range(pattern):
    print(" " *(pattern-1-i) + "*" + "  " * i + "*")