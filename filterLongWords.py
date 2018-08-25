class LongWordsFilter:
    def __init__(self):
        pass
    def doFilter(self, words, n):
        filteredWords=list(filter(lambda w: len(w)>n,words))
        return filteredWords

filtr=LongWordsFilter()
filteredWords=filtr.doFilter(['A','Dark','Horse','Rode','Through','The','Mountain'],4)
print("Filter list is given below:")
print(filteredWords)
