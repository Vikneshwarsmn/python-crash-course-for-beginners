'''
Tuples are
    1. used to store multiple items in a single variable.
    2. are ordered, unchangeable, and allow duplicate values
    3. are indexed, the first item has index [0], the second item has index [1] etc.

In tuples the items have a defined order, and that order will not change.
One cannot change, add or remove items after the tuple has been created.
tuples also allows duplicates
'''

avengers = ("captain america", "iron man", "hulk")
avengers = "captain america", "iron man", "hulk"
avengers = ()
avengers = ("captain america",)
avengers = "captain america",
len(avengers)

#
#tuples with different datatypes
tuple1 = ("captain america", "iron man", "hulk")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#tuples with mixedDataType
tuple1 = ("abc", 34, True, 40, "male")

#tuples creation with constructors
avengers = tuple(("captain america", "iron man", "hulk"))

#nested Tuples
avengersCoreTeam = ("captain america", "iron man", "hulk", "thor", "black widow", "hawk eye")
guardiansOfGalaxy = ("ant man", "star lord", "racoon", "gamora", "groot", "drax")

# nesting of tuples
avengersTeamInInfinityWar = avengersCoreTeam, guardiansOfGalaxy
avengersTeamInInfinityWar = (avengersCoreTeam, guardiansOfGalaxy)
