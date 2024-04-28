# syntax : for (variable) in (length)

# using for loop to add one to every element of a list.

x=[1,2,3,4,5,6,7,8,9]
y=[]

for i in x:
    y.append(i+1)

print(y)

# using for loop to separate numbers and strings 

x=["sarvagra","will","be","the","best","coder",1,69,3]
string=[]
number=[]

for i in x:
    if type(i) == int:
         number.append(i)
    else :
        string.append(i)

print("numbers=",number)
print("strings=",string)


