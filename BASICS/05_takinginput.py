# syntax: x=int(input("enter a number"))

marks = int(input("ENTER YOUR MARKS"))

if marks<30:
   print("Failed,try again!")
elif marks<=60 and marks>=30:
   print("Average!")
elif marks<80 and marks>60:
   print("GOOD!")
else:
   print("AMAZING!")

# taking input from user and then executes the code.