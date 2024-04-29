#syntax : [(outcome)(loop)(condition)]
# to square each element of a list using list comprehension

l=[1,2,3,4,5,6,7]
l2=[i**2 for i in l]
print(l2)

# to square each value in a dicitionary using dictionary comprehension
# for dictionary comprehension , first separate keys and values using dictionary.items()

d= {"k1": 1, "k2": 2, "k3":3, "k4":4}
s=d.items()
newd={k: v**2 for k,v in s}
print(newd)
