import re

txt = """Anki is a program which makes remembering things easy. Because it's a lot more efficient than traditional study methods, you can either greatly decrease your time spent studying, or greatly increase the amount you learn.
        Anyone who needs to remember things in their daily life can benefit from Anki. Since it is content-agnostic and supports images, audio, videos and scientific markup (via LaTeX), the possibilities are endless.
        For example:"""
num = """Member states agreed to 
    reduce their gas demand by 15 
    percent compared to their average 
    consumption in the past five years, 
    between 1 August 2022 and 31 March
    2023, with measures of their own 
    choice, the European Council said
     in a statement."""

word = []
word = txt.split()
w = re.compile(r'[A|B][A-Za-z]+')
#print('word:',word)
'''
for W in word:
    wl = w.match(W)
    
    if wl:
        print(W)
'''     
W = re.findall(w,txt)
print(W)
print(type(W))
for ww in W:
    print(ww)
   
m = re.compile(r'\d{1,4}')

nums = re.findall(m,num)
print(nums)

        