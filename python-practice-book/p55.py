def anagrams(lst):
	"""To find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example ‘eat’, ‘ate’ and ‘tea’ are anagrams."""
	
	word_dict = {}
	lengths = set(len(word) for word in lst)
	word_dict={length:[word for word in lst if  len(word)==length] for length in lengths}

	print(word_dict)
	

words = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
anagrams(words)
