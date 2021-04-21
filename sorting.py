#   what im going to do here:
#   1) import random and array to make random numbers inside an array
#   2) make a switch statement where a user can select what kind of sorting it wants to execute
#   3) implement bub sort using that list
#   4) implement select sort
#   5) how to do a insert and merge sort again ? 


# import random module to use random
import random as r
import array as arr





# function call to my sorting algos
#        
# selection sort 
def selection_Sort(mL):
    #check the length of the Array
    for i in range(len(mL)):
        #find the smallest value in the element inside the unsorted array
        minElement = i
        for j in range(i+1, len(mL)):
            # substitute the value of the minIndex if element[0] is greater than element[1]. 
            if mL[minElement] > mL[j]:
                minElement = j
        # swap the minimum element with the first index/element
        mL[i], mL[minElement] = mL[minElement] , mL[i]
        print(myList)
    return mL


def bubSort(myList):
    return myList

def inSort(myList):
    return myList

def merSort(myList):
    return myList









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

# choose a selection of sorting algo
print('''

choose a what sorting algo u want to see
1 = selection sort
2 = bubblesort
3 = insert sort
4 = merge sort
5 = exit


''')

chooseSort = input()

if chooseSort == "1":
    print(f"this your unsorted array: {myList}")
    selection_Sort(myList)
    print(f"result is: {myList}")
elif chooseSort == "2":
    bubSort(myList)
    print(myList)
elif chooseSort == "3":
    inSort(myList)
    print(myList)
elif chooseSort == "4":
    merSort(myList)
    print(myList)
else:
    print("enter numbers from 1 to 5 only thanks.")
    

