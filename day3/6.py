#day 3
#bonus
#program 6
#written by Syed Ali

sample_list = []
def subsetSums(arr, l, r, sum=0):
    # Print current list
    if l > r:
        sample_list.append(sum)
        return

    # list including arr[l]
    subsetSums(arr, l + 1, r, sum + arr[l])

    # list excluding arr[l]
    subsetSums(arr, l + 1, r, sum)

# Driver code
number = int(input("enter size of array"))
arr = []
for i in range(0,number):
    num = int(input())
    arr.append(num)
n = len(arr)
subsetSums(arr, 0, n - 1)
sample_list.remove(0) #Removing Zero From List
list_copy = []
for i in range(0,len(sample_list)):
    if sample_list[i] not in list_copy:
        list_copy.append(sample_list[i])

final_answer = []
count = 0

#To find minimum element not present in list

for i in range(0,len(list_copy)):
    if list_copy[i] not in arr:
        final_answer.append(list_copy[i])
#print(final_answer)

for i in range(0,len(final_answer)):
    t = i
    t += 1
    if t not in final_answer:
        if t not in arr:
            print(t)
            count += 1
if count == 0:
    max = final_answer[0]
    for i in range(0,len(final_answer)):
        if max < final_answer[i]:
            max = final_answer[i]

    print(max+1)