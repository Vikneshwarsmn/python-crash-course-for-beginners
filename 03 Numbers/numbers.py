'''
Number Types:
    int
    float
    complex

Build in Function:
    round() Rounds a numbers with the specified number of decimals i.e. round(number, decimals)
'''
# The basics
3 + 2  # addition
3 - 2  # subtraction
3 * 2  # multiplication
3 / 2  # classic division returns a float

# Modulus
20 // 3  # floor division discards the fractional part
20 % 3  # the % operator returns the remainder of the division
divmod(20, 3)

# Exponentiation (power of)
3 ** 2
2 ** 7
pow(2, 7)

# Using variables
weight = 70
height = 1.75  # in meters
bmi = weight / (height ** 2)
round(bmi, 2)
