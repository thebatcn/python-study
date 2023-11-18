words ='d DDD sd1'
newwords=''

newwords = filter(lambda x: x.isalpha() or x==' ', words)
print(list(newwords))
# for i in words:
#     if not i.isalpha():
#         continue
#     else:
#        newwords= ''.join(i.lower())  
# print(newwords)
# W =[str.lower(w) for w in words.split() ]


# print(W)