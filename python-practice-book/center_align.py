import sys
file = sys.argv[1]
#file = 'she.txt'
fp =  open(file,'r')
num_max_line =len(max(fp))
print(num_max_line)
#fp =  open('she.txt','r')
fp.seek(0)
for word_line in fp:
	print(word_line.center(51))