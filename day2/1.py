#Day2
#Program1

import math

user_number = int(input("Input a number for various operations"))

#OPeartion 1
print("\nOperation 1 - Check whether Odd/Even")
if user_number % 2 == 0 and user_number != 0:
    print(user_number," is an Even Number")
elif user_number % 2:
    print(user_number," is an Odd Number")

#Operation 2
print("\nOperation 2 - Check whether prime or not")
count=0
for i in range(1,user_number+1):
    if user_number % i == 0:
        count = count+1
if count == 2 :
    print(user_number," is a Prime number")
else :
    print(user_number," is not a Prime number")

#Operation 3
print("\nOperation 3 - check whether palindrome or not")
user_number_2 = str(user_number) #12
rev_number = ""
for i in range(len(user_number_2)-1,-1,-1):
    rev_number += user_number_2[i];
rev_number = int(rev_number)

if rev_number == user_number:
    print(user_number," is a palindrome number")
else:
    print(user_number," is not a palindrome number")

#Operation 4
print("\nOperation 4 -  for checking Armstrong")
length_user_number = len(user_number_2)
rem=0
sum_number =0
num=user_number
for i in range(length_user_number):
    rem = num % 10
    sum_number = sum_number + pow(rem,length_user_number)
    num = num // 10
if sum_number == user_number:
    print(user_number," is an Armstrong number")
else:
    print(user_number," is not an Armstrong number")


