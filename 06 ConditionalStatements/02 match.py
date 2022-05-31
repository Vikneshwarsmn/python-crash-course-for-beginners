'''
Structural pattern matching has been added in the form of a match
statement and case statements of patterns with associated actions.
Patterns consist of sequences, mappings, primitive data types as
well as class instances. Pattern matching enables programs to extract
information from complex data types, branch on the structure of data,
and apply specific actions based on different forms of data.

A match statement takes an expression and compares its value to
successive patterns given as one or more case blocks.

Note: We have a class in this demo. Don't get too caught up in how it
works! We have a class video in this course :)
'''


def findTheAvengerBasedOnPowers(powers):
    match powers:
        case 'superhuman':
            print('Captain America')
        case 'arrows':
            print('Hawk Eye')
        case 'human':
            print('Black Widow')
        case 'smash':
            print('Hulk')
        case _:
            print('Avengers member not found')


findTheAvengerBasedOnPowers('superhuman')
findTheAvengerBasedOnPowers('arrows')
findTheAvengerBasedOnPowers('human')
findTheAvengerBasedOnPowers('blah')
