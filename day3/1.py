#Day-3
#program-1

str = input("Enter a String to be reversed")
reverse_string = ""
for i in range(len(str)-1,-1,-1):
    reverse_string = reverse_string + str[i]
print(reverse_string)