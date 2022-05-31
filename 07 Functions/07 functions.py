'''
Think of a function as a little named container for a group of your code!
To run the code in a function, you must call the function.

A function can be called from anywhere after the function is defined.

Functions can return a value using a return statement. Functions are
a common feature among all programming languages

There are 3 forms of function arguments
    Position only arguments
    Positional or keyword arguments
    Keyword only arguments (named parameters)
'''


# basics
def function1(user):
    printMessage = "Hello {0} !!!".format(user)
    print(printMessage)


function1("Thor")


# function arguments
def functionWithOneArgument(arg):
    print(arg)


functionWithOneArgument("single argument function")


def functionWithMultipleArguments(realName, superheroName):
    printMessage = realName + " is " + superheroName
    print(printMessage)


functionWithMultipleArguments("steve rogers", "captain america")
functionWithMultipleArguments("tony stark", "iron man")


# Arbitrary Arguments, *args
def functionWithArbitraryArguments(*superheroes):
    print("The Superhero is " + superheroes[0])
    print("The Superhero is " + superheroes[1])
    print("The Superhero is " + superheroes[2])


functionWithArbitraryArguments("captain america", "iron man", "black widow")


# function with keyword arguments
def functionWithKeywordArguments(superhero1, superhero2, superhero3):
    print("The Superhero is " + superhero1)
    print("The Superhero is " + superhero2)
    print("The Superhero is " + superhero3)


functionWithKeywordArguments(superhero1="captain america", superhero2="thor", superhero3="iron man")


# function with Arbitrary Keyword Arguments, **kwargs
def functionWithArbitraryKeywordArguments(**superhero):
    message = "His name is {} and he is called {}"
    printMessage = message.format(superhero["realName"], superhero["superheroName"])
    print(printMessage)


functionWithArbitraryKeywordArguments(realName="steve rogers", superheroName="captain america")


def functionWithDefaultArguments(superhero="captain america"):
    message = "My name is {} and I'm an Avenger."
    printMessage = message.format(superhero)
    print(printMessage)


functionWithDefaultArguments("hulk")
functionWithDefaultArguments("iron man")
functionWithDefaultArguments("hawk eye")
functionWithDefaultArguments()
