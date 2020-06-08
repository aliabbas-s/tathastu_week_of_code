#Day-3
#Program 3

string = input("Enter a Word")
length = len(string)
duplicate_string = ""
for i in range(0,length):
    if string[i] in duplicate_string:
        continue
    else:
        duplicate_string += string[i]
print(duplicate_string)
