# first line of python refiresher!

print("hello world!")

# variable time!

a = 25          # int
b = 1.5         # float
c = "Hello!"    #string
d = True        # boolean
e = None        # noneType

print(a)
print(b)
print(c)
print(d)
print(e)


# request for input to the user! 

name = input("name:")
print("hello", name)

# Formatted strings substitute a variable of a number

name = input("name again? :")
print(f"hello {name}")

# conditions

n = int(input("Enter a number: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
