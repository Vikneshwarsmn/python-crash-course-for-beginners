'''
Python’s for statement iterates over the items of any sequence
(a list or a string), in the order that they appear in the
sequence.

The built-in Range function 'range()' comes in handy if you do need
to iterate over a sequence of numbers. It generates arithmetic progressions:

range(start, stop, step)
start
The value of the start parameter (or 0 if the parameter was not supplied)
stop
The value of the stop parameter
step
The value of the step parameter (or 1 if the parameter was not supplied)
'''

# The basics
topZombieMovies = ['resident evil', 'train to busan', 'zombieland', 'warm bodies', 'world war z']
for movie in topZombieMovies:
    print(movie)

# using the range function
for i in range(5):
    print(i)

# range(start, stop, step)
list(range(5, 10))
list(range(0, 10, 3))
list(range(-10, -100, -30))

topZombieMovies = ['resident evil', 'train to busan', 'zombieland', 'warm bodies', 'world war z']
for i in range(len(topZombieMovies)):
    print(topZombieMovies[i])

# Create a sample collection
movies = {
    'resident evil': 'watchlist',
    'train to busan': 'watchlist',
    'zombieland': 'watchlist',
    'warm bodies': 'watchlist',
    'world war z': 'watched'
    }

# Strategy:  Iterate over a copy
for movie, status in movies.copy().items():
    print(movie)
    print(status)
    if status == 'watched':
        del movies[movie]
movies

# Strategy:  Create a new collection
watchedMovies = {}
watchlistMovies = {}
for movie, status in movies.items():
    if status == 'watched':
        watchedMovies[movie] = status
    else:
        watchlistMovies[movie] = status
