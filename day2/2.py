#Day 2
#Program -2

number  = int(input("Enter the nth number till fibonacci you want"))
first_number = 0
second_number = 1
for i in range(number):
    if(i <= 1):
        third_number = i
    else:
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number

    if i == number-1:
        print(third_number)
    else:
        print(third_number,end = ",")