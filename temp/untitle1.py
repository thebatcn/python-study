x = [i for i in range(1,10)]
print(x)
print(str.casefold('ADFDASEFsdfae'))
#dict.copy()
class X():

    def __init__(self, J):
        self.J = J

    def M(self, J):
        pass

foo = X('A')
print(foo)

print(foo.M('B'))
foo.K = 'q'

boo = X("pp")

print("foo.K = {}".format,foo.K)

foo.K

Dict = {x:x*2 for x in range(1,6)}
print(Dict)
del Dict[2]
print(Dict)
Dict.clear()
print(Dict)
del Dict
print(Dict)
