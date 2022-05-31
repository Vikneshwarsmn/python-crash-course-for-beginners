'''
Sets are
    1. used to store multiple items in a single variable.
    2. unordered, unchangeable*, and unindexed.
    3. do not allow duplicate values.

In tuples the items do not have a defined order, and items can appear in a different
order every time you use them, and cannot be referred to by index or key.
Once a set is created, you cannot change its items, but you can remove items and add new items.
'''

avengers = {"captain america", "iron man", "hulk"}
len(avengers)

#set with different datatypes
set1 = {"captain america", "iron man", "hulk"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#set with mixedDataType
set1 = {"abc", 34, True, 40, "male"}

avengers = set(("captain america", "iron man", "hulk"))

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a # unique letters in a
a - b # letters in a but not in b
a | b # letters in a or b or both
a & b # letters in both a and b
a ^ b # letters in a or b but not both
