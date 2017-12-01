# Cheatsheet Python Set
# set loop sequence is unstable!
set1 = set()                        # A new empty set
set1.add("cat")                     # Add a single member
set1.update(["dog", "mouse"])       # Add several members
if "cat" in set1:                   # Membership test
  set1.remove("cat")
#set1.remove("elephant")            # throws an error
set1.discard("elephant")            # No error thrown
print(set1)
for item in set1:                   # Iteration AKA for each element
    print(item)
print("count:{}".format(len(set1))) # Length AKA size AKA item count
isempty = len(set1) == 0            # Test for emptiness
set1 = set(["cat", "dog"])          # Initialize set from a list
set2 = set(["dog", "mouse"])
set3 = set1 & set2                  # Intersection
set4 = set1 | set2                  # Union
set5 = set1 - set3                  # Set difference
set6 = set1 ^ set2                  # Symmetric difference
issubset = set1 <= set2             # Subset test
issuperset = set1 >= set2           # Superset test
set7 = set1.copy()                  # A shallow copy
set7.remove("cat")
set8 = set1.copy()
set8.clear()                        # Clear AKA empty AKA erase
print((set1, set2, set3, set4, set5, set6, set7, set8, issubset, issuperset))
