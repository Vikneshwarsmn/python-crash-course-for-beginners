'''
Lists are
    1. Used to store multiple items in a single variable.
    2. are ordered, changeable, and allow duplicate values.
    3. are indexed, the first item has index [0],
        the second item has index [1] etc.

In lists the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at
the end of the list.

One can change, add, and remove items in a list after it has been created.
List also allows duplicates
'''

# unique value
avengers = ["captain america", "iron man", "hulk"]

# duplicate values
avengers = ["captain america", "iron man", "hulk", "hulk", "hulk"]

listLength = len(avengers)

# data types of list
guardiansOfGalaxy = ["star lord", "racoon"]
numbers = [1, 5, 7, 9, 3]
booleanValues = [True, False, False]

# list of mixed data Types
mixedDataTypeList = ["abc", 34, True, 40, "male"]

# create list using constructors
avengersCoreTeam = list(("captain america", "iron man", "hulk", "thor", "black widow", "hawk eye"))
print(avengersCoreTeam)

# list Concatenation
avengersCoreTeam = ["captain america", "iron man", "hulk", "thor", "black widow", "hawk eye"]
guardiansOfGalaxy = ["ant man", "star lord", "racoon", "gamora", "groot", "drax"]

avengersInfinityWarTeam = avengersCoreTeam + guardiansOfGalaxy
