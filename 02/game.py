#!python3
#game.py

    
import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    letters = random.choices(POUCH , k = NUM_LETTERS)
    return letters
    


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    print("Your letters are %s " % (draw))
    word = input("Input a word from your letters")
    valid = _validation(word,draw)
    if valid == True:
        return word
    else:
        return "Please enter a valid word and try again"
    



def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    switch = True
    while switch:
        for letter in word:
            if letter in draw:
                continue
            else:
                return "You don't have that letter"
                
        if word in DICTIONARY:
            print("%s is a valid word" % (word))
            return True
        else:
            print("This is not a valid word. Try again")
            return False


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)



def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    combos =_get_permutations_draw(draw)
    lst = []
    for i in combos:
        if i in DICTIONARY:
                  lst.append(i)
    return lst
    


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters."""
    perm = itertools.permutations(draw)
    return perm



# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()

