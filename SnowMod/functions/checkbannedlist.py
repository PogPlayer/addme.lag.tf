import re

def isbanned(list, word):
    for x in list:
        if re.search(x, word):
            return x
        else:
            return False