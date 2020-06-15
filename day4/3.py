#Day-4
#Program-3

dict_main = {
    "hello":150,
    "ali":52,
    "abbas":200,
    "syed":10}
list_copy=[]
dict_val = list(dict_main.values())
max = dict_val[-1]
list_copy.append(max)
for i in range(len(dict_val)-2,-1,-1):
    if max < dict_val[i]:
        max = dict_val[i]
dict_val.remove(max)

max_2 = dict_val[-1]
for i in range(len(dict_val)-2,-1,-1):
    if max_2 < dict_val[i]:
        max_2 = dict_val[i]
print("the second maximum value is ",max_2)