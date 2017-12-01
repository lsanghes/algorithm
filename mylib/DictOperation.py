# Cheatsheet Python Dictionary
# dict loop sequence is unstable!

# max(dict) return max key
# max(dict, key=lambda x:dict[x]) return max value

dict1 = {}                     # Create an empty dictionary
dict2 = dict()                 # Create an empty dictionary 2
dict2 = {"r": 34, "i": 56}     # Initialize to non-empty value
dict3 = dict([("r", 34),
              ("i", 56)])      # Init from a list of tuples
dict4 = dict(r=34, i=56)       # Initialize to non-empty value 3
dict1["temperature"] = 32      # Assign value to a key
if "temperature" in dict1:     # Membership test of a key AKA key exists
  del dict1["temperature"]     # Delete AKA remove
equalbyvalue = dict2 == dict3
itemcount2 = len(dict2)        # Length AKA size AKA item count
isempty2 = len(dict2) == 0     # Emptiness test
for key in dict2:              # Iterate via keys
  print((key, dict2[key]))     # Print key and the associated value
  dict2[key] += 10             # Modify-access to the key-value pair
for value in dict2.values():   # Iterate via values
  print(value)
dict5 = {x: dict2[x] + 1 for x in dict2 } # Dictionary comprehension
dict6 = dict2.copy()             # A shallow copy
dict6.update({"i": 60, "j": 30}) # Add or overwrite
dict7 = dict2.copy()
dict7.clear()                  # Clear AKA empty AKA erase
print((dict1, dict2, dict3, dict4, dict5, dict6, dict7, equalbyvalue, itemcount2))

# setdefault(key[, default])
#   If key is in the dictionary, return its value.
#   If not, insert key with a value of default and return default.
#   default defaults to None.

# get(key[, default])
#     Return the value for key if key is in the dictionary, else default.
#     If default is not given, it defaults to None, so that this method never
#     raises a KeyError.
