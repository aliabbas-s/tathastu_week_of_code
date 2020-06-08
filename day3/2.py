#day-3
#program 3

def permutations(s,i,n):
    if(i == n-1):
        print("".join(s),end=" ")
    else:
        for j in range(i,n): #ALi
            s[i],s[j] = s[j],s[i]
            permutations(s,i+1,n)
            s[i],s[j] = s[j],s[i]


str = input("Enter a String")
length=len(str)
s = list(str)
permutations(s,0,length)


