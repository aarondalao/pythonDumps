#A set is a collection of unique values
# create a set
s = set()

#add elements to the set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(4)
print(s) # take note that code line #11 "s.add(4)" is NOT printed TWICE in the output

s.remove(2) 
print(s)

# len will give the length of a list,tuple,set, etc

print(f"the set has {len(s)} elements.")