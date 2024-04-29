''' syntax : while (condition)
                statements          '''

# printing numbers from 1 to 10 and finding their sum.

n=int(input("ENTER THE NUMBER UPTO WHICH SUM HAS TO BE PRINTED"))
sum1=0
i=0
while i<=n:
        sum1=sum1+i
        i+=1
    
print("SUM=",sum1)


# program to find the factorial of any number input by user

n=int(input("ENTER THE NUMBER OF WHICH THE FACTORIAL HAS TO BE PRINTED"))
prod=1
i=1

if n>0:
    while i<=n:
            prod*=i
            i+=1

    print("FACTORIAL =",prod)


# program to print fibonacci series upto given nnumber of elements

n=int(input("ENTER THE NUMBER OF WHICH THE FACTORIAL HAS TO BE PRINTED"))
a,b=0,1
i,s=0,0
print("FIBONACCI SERIES UPTO",n,"TERMS:")

while i<n:
    s=a+b
    print(a)
    a=b
    b=s
    i+=1
    
# program to reverse a string input by user

s=input("ENTER THE STRING TO BE REVERSED")
rev=""
length=len(s)

while length>0:
    rev=rev+s[length-1]
    length-=1
    
print(rev)

    
       
