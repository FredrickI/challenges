from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY) as d:
        return [word.rstrip() for word in d.read().split()]
    

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    count = 0
    for letter in word:
        count += LETTER_SCORES[letter.upper()]
    return count

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
