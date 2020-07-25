# Optimal Solution
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(funct=None):  return funct(0) if funct else 0
def one(funct=None):   return funct(1) if funct else 1
def two(funct=None):   return funct(2) if funct else 2
def three(funct=None): return funct(3) if funct else 3
def four(funct=None):  return funct(4) if funct else 4
def five(funct=None):  return funct(5) if funct else 5
def six(funct=None):   return funct(6) if funct else 6
def seven(funct=None): return funct(7) if funct else 7
def eight(funct=None): return funct(8) if funct else 8
def nine(funct=None):  return funct(9) if funct else 9

# Currying (Returning a function)
def plus(i2):       return lambda i1: i1 + i2
def minus(i2):      return lambda i1: i1 - i2
def times(i2):      return lambda i1: i1 * i2
def divided_by(i2): return lambda i1: i1 // i2