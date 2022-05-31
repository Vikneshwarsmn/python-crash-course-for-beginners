# Python control flows - If statement

'''
If a condition is met, do something...
else do something different!

'elif' stands for 'else if'

both elif and else are optional!
'''

# The basics
def findTheAvengerBasedOnPowers(powers):
    if powers == "superhuman":
        print('Captain America')
    elif powers == "arrows":
        print('Black Widow')
    elif powers == "human":
        print('Black Widow')
    elif powers == "smash":
        print('Hulk')
    else:
        print('Avengers member not found')


findTheAvengerBasedOnPowers('superhuman')
findTheAvengerBasedOnPowers('arrows')
findTheAvengerBasedOnPowers('human')
findTheAvengerBasedOnPowers('smash')
findTheAvengerBasedOnPowers('something')
