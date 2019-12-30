import math
import random

from decimal import *



#used to limit fraction dfficulty for generate_fraction() method
fraction_max_component = 15

#   Custom fraction class
#   Contains functions for generating and printing fractional numbers. Supported mathematical operations:
#   int*fraction
#   fraction*fraction
#   fraction - fraction
#   fraction + fraction
#   fraction /fraction
#
#   Useful functions
#   __init__ (a,b) returns fraction a/b
#   __str__ returns the fraction as text
#   simplifySelf() simplifies the fraction with greatest common divisor, internal function
#   get_latex() returns fraction in latex format without $$, dollar signs are added later if needed
#   get_latex_mixed_fraction() returns fraction in mixed fraction format. eq 5/2 = 2 1/2


#   Other functions within file
#   generate_fraction() returns random fraction with fraction_max_component as the highest possible numerator or denominator
#   fraction_from_decimal turns decimal number to fraction and returns the simplified fraction


class fraction:
    def __init__(self, val1, val2):
        self.numerator = val1
        self.denominator = val2
        self.simplifySelf()

    def __str__(self):
        return str(self.numerator) + "/" +str(self.denominator)

    def __mul__(self, val):
        #allows fractions to be multiplied by ints or other fractions
        newNumerator = 0
        newDenominator = 0
        if(isinstance(val, int)):
            newNumerator = self.numerator * val
            newDenominator = self.denominator
        elif(isinstance(val, fraction)):
            newNumerator = self.numerator * val.numerator
            newDenominator = self.denominator * val.denominator
        #generated fraction can at times be simplified
        newFraction = fraction(newNumerator, newDenominator)
        newFraction.simplifySelf()
        return newFraction

    def __add__(self, val):
        #Supports adding ints and fractions
        newNumerator = 0
        newDenominator = 0
        if(isinstance(val, int)):
            newNumerator = self.numerator + val*self.denominator
            newDenominator = self.denominator
        if(isinstance(val, fraction)):
            newDenominator = self.denominator*val.denominator
            newNumerator = self.numerator*val.denominator + self.denominator*val.numerator

        newFraction = fraction(newNumerator, newDenominator)
        newFraction.simplifySelf()
        return newFraction

    def __sub__(self, val):
        newVal = val*(-1)
        return self + newVal

    def __truediv__(self, val):
        newFraction = fraction(self.numerator*val.denominator, self.denominator*val.numerator)
        newFraction.simplifySelf()
        return newFraction

    def __eq__(self, other):
        if(self.numerator == other.numerator and self.denominator == other.denominator):
            return True

        return False


    def simplifySelf(self):
        #Simplifies 3/6 to 1/2, uses greatest common divisor and casts back to int
        simplifyBy = math.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / simplifyBy)
        self.denominator = int(self.denominator / simplifyBy)

    def get_latex(self):
        return r"\frac{" + str(self.numerator) + "}{" + str(self.denominator) + "}"

    def get_latex_mixed_fraction(self):
        #returns the fraction in the shape of a mixed fraction
        remainingNumerator = self.numerator % self.denominator
        integerPart = int((self.numerator- remainingNumerator)/self.denominator)
        #print("integer part:" + str(integerPart) + "remainingNumerator" + str(remainingNumerator))

        if(integerPart == 0):
            return self.get_latex()
        elif(remainingNumerator == 0):
            return str(integerPart)
        else:
            return str(integerPart) + r"\frac{" + str(remainingNumerator) + "}{" + str(self.denominator) + "}"



    def absolute_value(self):
        return self.numerator/self.denominator






def generate_fraction():
    #generates fractions, restricted to fractions with absolute value lower than 3
    newFraction = fraction(random.randint(1,fraction_max_component), random.randint(1,fraction_max_component))

    while (True):
        if(newFraction.absolute_value() > 3):
            newFraction = fraction(random.randint(1,fraction_max_component), random.randint(1,fraction_max_component))
        else:
            break


    return newFraction


#returns a fraction when given a decimal
def fraction_from_decimal(decimal):
    #I take that back, this is actually pretty neat

    multiplierUsed = 10
    while(True):
        forcedInt = Decimal(int(decimal*multiplierUsed))
        forcedDecimal = decimal*multiplierUsed
        #if these numbers are the same
        #then multiplier is high enough

        #print("numbers: " + str(forcedInt) + "and" + str(forcedDecimal))

        if(forcedInt == forcedDecimal):
            #print("FOUND at" + str(multiplierUsed))
            break
        else:
            multiplierUsed*=10

        #now we should have the right multiplier
    return fraction(int(decimal*multiplierUsed), multiplierUsed)
