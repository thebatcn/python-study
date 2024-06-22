def wordwrap(file,nums_words):
	with open(file,'r') as fp:
		words_list = fp.read().split()
		#print(words_list)
	#n =0
#	for i in fp:
#		n+=1
#	print(n)
	#n=0

	return (' '.join(words_list[:20]))
	
print(wordwrap('she.txt',12))