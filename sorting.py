#   what im going to do here:
#   1) import random and array to make random numbers inside an array
#   2) make a switch statement where a user can select what kind of sorting it wants to execute
#   3) implement bub sort using that list
#   4) implement select sort
#   5) how to do a insert and merge sort again ? 




# import random module to use random
import random as r
import array as arr

# setting up input range
x = int(input("Enter the start number you want to randomly generate:"))
y = int(input("Enter the end number you want to randomly generate:"))
print(x,y)

# setting up random list
# then fill up the randomList with random number. if the number not a duplicate insert into the list
z = int(input("Enter the size of your array:"))

myList = arr.array('i',[])
for i in range(z):
    n = r.randint(x,y)
    #if n not in myList: #trying to 
    myList.append(n)    
       

print(myList)