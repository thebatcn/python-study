def valuesort(D):
    """to sort values of a dictionary based on the key"""
    
    # result = dict(sorted(D.items(), key=lambda x:x[0]))
    # return list(result.values())
    
    sorted_dict = sorted(D.items(), key=lambda x:x[0])
    return [value for key,value in sorted_dict]
    
cc

print(valuesort(onedict))