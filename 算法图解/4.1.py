def sum(x):
    if not x:
        return 0
    # elif len(x)==1:
    #     return x[0]
    else:
        return x[0] + sum(x[1:])


a = [1,2,3,4,5,6]

# print(a[1::2])
print(sum(a))