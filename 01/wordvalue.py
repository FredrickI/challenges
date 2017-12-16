from data import DICTIONARY, LETTER_SCORES

def load_words():
    dict = open(DICTIONARY, 'r+')
    lst = []
    for i in dict:
        lst.append(i)
    lst = [word.rstrip() for word in lst]
    return lst
    

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[letter] for letter.upper() in word]

def max_word_value(words):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    counter = 0
	for word in words:
		if calc_word_value(word) > counter:
			counter = calc_word_value(word)
	       		max_word = word
		else:
			continue
	return "%s is the word with a max value of %s" % (max_word, counter)

if __name__ == "__main__":
    pass # run unittests to validate
