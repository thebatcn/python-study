import re

def displaymatch(matchobj):
    if matchobj is None:
        return None
    return '<Match: %r, groups=%r>' % (matchobj.group(), matchobj.groups())

# valid = re.compile(r'^[a2-9tjqk]{5}$')
valid = re.compile(r"^[a2-9tjqk]{5}$")
pair = re.compile(r".*(.).*\1")
print(displaymatch(valid.match('akt5q')))
# print(valid.match('akt5q'))
print(displaymatch(pair.match('a22tt'))) #两个对子不适用？
