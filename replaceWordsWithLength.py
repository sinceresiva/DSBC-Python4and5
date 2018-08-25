class ReplaceWordsWithLength:
    def __init__(self):
        pass
    def getNewList(self, words):
        newList=[str(len(w)) for w in words]
        return newList

replacer=ReplaceWordsWithLength()
newList=replacer.getNewList(['A','Dark','Horse','Rode','Through','The','Mountain'])
print("The new list is given below:")
print(newList)
