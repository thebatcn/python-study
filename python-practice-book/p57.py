def invertdict(D):
    """a function invertdict to interchange keys and values in a dictionary"""
    result = {value:key for key, value in D.items()}
    return result

onedict = {'x':1,'y':2,'a':3}

print(invertdict(onedict))