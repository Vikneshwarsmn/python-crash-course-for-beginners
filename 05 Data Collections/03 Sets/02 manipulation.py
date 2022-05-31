
avengers = {"captain america", "iron man", "hulk", "thor", "black widow"}
guardiansOfGalaxy = {"ant man", "star lord", "racoon", "gamora", "groot", "drax"}

# add() Adds an element to the set
avengers.add("hawk eye")

# update() Update the set with another set, or any other iterable
# Update with a set
avengers.update(guardiansOfGalaxy)

# Update with a List
guardiansOfGalaxy = ["ant man", "star lord", "racoon", "gamora", "groot", "drax"]
avengers.update(guardiansOfGalaxy)

# copy() Returns a copy of the set
avegersNewList = avengers.copy()

# difference() Returns a set containing the difference between two or more sets
avengersNewList.difference(guardiansOfGalaxy)

# difference_update() The difference_update() method removes the items that exist in both sets.
avengersCoreTeam = {"captain america", "iron man", "hulk", "thor", "black widow", "hawk eye"}
avengersInfinityWarTeam = {"captain america", "iron man", "hulk", "thor", "black widow", "hawk eye",
                                "doctor strange", "ant-man", "spider-man", "star-lord", "drax"}

avengersInfinityWarTeam.difference_update(avengersCoreTeam)

# remove() Removes the specified element
avengers.remove("gamora")

# discard() Remove the specified item
avengers.discard("gamora")

# pop() Removes an element from the set
avengers.pop()

# clear() Removes all the elements from the set
avengers.clear()

# delete the set
del avengers
