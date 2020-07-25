# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
# First solution
'''
def pig_it(text):
    return " ".join([s[1:] + s[0] + "ay" if s not in "?!." else s for s in text.split(' ')])
'''

# Refactored solution
def pig_it(text):
    return " ".join([f"{s[1:]}{s[0]}ay" if s not in "?!." else s for s in text.split(' ')])