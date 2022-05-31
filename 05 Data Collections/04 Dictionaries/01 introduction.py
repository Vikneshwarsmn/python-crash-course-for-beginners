#Using python to manipulate dictionary

'''
Python knows a number of compound data types, used to group together other values.
One of the most used is a dictionary. Dictionaries are used to store data values
in key:value pairs.

Dictionaries are mutable - this means that item values can be changed
'''

#The basics
movieDictionary = {
    'movieName': 'Avengers: EndGame',
    'releaseDate': '26 April 2019',
    'directors': "['Joe Russo', 'Anthony Russo']",
    'producers': ['Kevin Feige']
}

movieDictionary[0]  # this will return an error as you need to ref the key by name
movieDictionary['movieName']

# copy() Returns a copy of the dictionary
movieDictionaryV1 = movieDictionary.copy()

# altering a dict
movieDictionaryV1['producers'] = ''
movieDictionaryV1['movieName'] = ''

#Length
len(movieDictionaryV1)

# update() Updates the dictionary with the specified key-value pairs
movieDictionary.update({"genre": "Action/Fantasy/Superhero"})

# keys() Returns a list containing the dictionary's keys
movieDictionary.keys()

# values() Returns a list of all the values in the dictionary
movieDictionary.values()

# get() Returns the value of the specified key
movieDictionary.get('producers')
movieDictionary.get("producers")
movieDictionary["producers"]

# items() Returns a list containing a tuple for each key value pair
movieDictionary.items()

# pop() Removes the element with the specified key
movieDictionary.pop('producers')

# popitem() Removes the last inserted key-value pair
movieDictionary.popitem()

# fromkeys() Returns a dictionary with the specified keys and value
dict.fromkeys(movieDictionary)

# setdefault() Returns the value of the specified key. If the key does not exist:
# insert the key, with the specified value
movieDictionary.setdefault("genre")
movieDictionary.setdefault("producers", "Kevin Fiege")

# clear() Removes all the elements from the dictionary
movieDictionary.clear()
