
# cannot change tuple value but once converting it to list we can modify

avengers = ("captain america", "superman", "hulk", "thor", "black widow", "hawk eye")

avengers = list(avengers)
avengers[1] = "iron man"
avengers = tuple(avengers)

# add new
avengers = list(avengers)
avengers.append("iron man")

#count
avengers.count("superman")

#index
avengers.index("superman")


# delete
del avengers
