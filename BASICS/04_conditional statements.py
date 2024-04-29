# if :if the given condition is true , it executes the next statement or the control moves out of if block, not executing the if block.

marks =40
if marks>30:
   print("passed!")

#if marks are greater than 30 , then print "passed!" else ignore the if block. 


# if-else :if the given condition is true , it executes the next statement , if it is false , else block is executed.

marks =25

if marks>30:
   print("Passed!")
else:
   print("Failed,try again!")

# as marks are <30, if vlock is ignored and else block is executed.

#elif :this is used to add multiple conditions 
 
marks = 75 

if marks<30:
   print("Failed,try again!")
elif marks<=60 and marks>=30:
   print("Average!")
elif marks<80 and marks>60:
   print("GOOD!")
else:
   print("AMAZING!")     

""" this prints :
    "failed,try again!" when marks are below 30
    "average!" if marks are 30-60
    "good!" if marks are 60-80
    "amazing" if marks are above 80, that is, else block """ 


