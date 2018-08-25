'''
Function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
'''

class VowelFinder:
    def __init__(self):
        pass
    def isVowel(self, chr):
        return chr.lower() in ['a','e','i','o','u']

chr=input("Enter a character:")
vFinder=VowelFinder()
result = vFinder.isVowel(chr)
print(result)
