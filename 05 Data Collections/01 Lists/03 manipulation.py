avengers = ["captain america", "iron man", "hulk", "thor", "black widow", "hawk eye"]
guardiansOfGalaxy = ["ant man", "star lord", "racoon", "gamora", "groot", "drax"]

#copy() Returns a copy of the list
avengersList1  = avengers[:]
avengersList2 = avengersCoreTeam.copy()
avengersList3 = list(avengersList1)

#append() Adds an element at the end of the list
avengers.append("doctor strange")

#count() Returns the number of elements with the specified value
avengers.count("doctor strange")

#insert() Adds an element at the specified position
length = len(avengers)
avengers.insert(length, "star-lord")

#index() Returns the index of the first element with the specified value
avengers.index("hulk")

#extend() Add the elements of a list (or any iterable), to the end of the current list
avengers.extend(guardiansOfGalaxy)

# updating list values
avengers = ["captain america", "superman", "hulk", "thor", "black widow", "hawk eye"]
avengers[1] = "iron man"

#remove() Removes the first item with the specified value
avengers.remove("captain america")

# pop() Removes the element at the specified position
avengers.pop(1)

#clear() Removes all the elements from the list
avengers.clear()

#reverse() Reverses the order of the list
avengers.reverse();

#sort() Sorts the list
avengers.sort()

#del
del avengers[0]
del avengers
