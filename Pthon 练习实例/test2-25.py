# test if any word in needle ends in ('ly', 'ed', 'ing', 'ers'):

# suffixes = ('ly', 'ed', 'ing', 'ers')
# # needle = 'foo'
# needle = 'fooly'
# any(needle.endswith(suffix) for suffix in suffixes)

# a = [1.2,0,8]
# b = any(isinstance(x,int) for x in a)

# print(b)

# c = {x:x**3 for x in range(1,11)}
# print(c)

# d = dict([(x,x**3) for x in range(1,11)])
# print(d)

strs = 'BCDEFGH'

def reverseString(strings):
    reversed_string = ""
    
    for char in strings:
        reversed_string = char + reversed_string
    return reversed_string

print(strs)
newstrings = reverseString(strs)
print(newstrings)