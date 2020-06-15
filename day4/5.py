#Day 4
#program 5

array_candidates = input("Enter Names For vote followed by spaces")
array_candidates = array_candidates.strip().lower().split(" ")
dict_array = {}
count = 0
#base case
if len(array_candidates) == 1:
    print ( "Cant Be Left Empty")
else:
    for i in range(0,len(array_candidates)):
        for j in range(0,len(array_candidates)):
            if array_candidates[i] == array_candidates[j]:
                count += 1
        dict_array[array_candidates[i]] = count
        count = 0
    print("Votes different candidates got : ",dict_array)

    list_key = list(dict_array.keys())
    list_value = list(dict_array.values())
    max = list_value[0]
    dic_hold_max = {}
    dic_hold_max[list_key[0]] = list_value[0]
    for i in range(1,len(dict_array)):
        if max < list_value[i] or max == list_value[i]:
            if max < list_value[i]:
                max = list_value[i]
                dic_hold_max.clear()
            max = list_value[i]
            dic_hold_max[list_key[i]] = max
    print("Votes gained maximum by : ",dic_hold_max)

    #lexicographic checking
    list_key = list(dic_hold_max.keys())
    list_value = list(dic_hold_max.values())
    maximum = list_key[-1]

    for i in range(len(list_key)-2,-1,-1):
        if maximum > list_key[i] :
            maximum = list_key[i]
    print("Winner of election is-", maximum)