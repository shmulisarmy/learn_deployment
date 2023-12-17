import sys
import string
import random
from resources.word_dictionary import * 
from resources.store_sentence_choices import *
from tree_maker import *

letter_counts_example = {i: random.randint(1, 30) for i in string.ascii_lowercase + ' '}
sentence_tree_d = make_full_tree(sentence_counters)
word_trees_d = {i: make_full_tree(word_replacement_dict[i]) for i in word_replacement_dict}
test_generation_amount = int(sys.argv[1]) if len(sys.argv) > 1 else 1

def select_word_using_most_common_letters(word_list_tree, letter_counts_dict):
    # print(letter_counts_dict)
    word = []
    while True:
        availible_letters = list(filter(lambda x: x in letter_counts_dict, word_list_tree.letters))

        if not availible_letters:
            return ''.join(word)
            
        most_common_availible_letter = max(availible_letters, key = lambda letter: letter_counts_dict[letter])
            
        letter_counts_dict[most_common_availible_letter] -= 1
        word.append(most_common_availible_letter)
        word_list_tree = word_list_tree.letters[most_common_availible_letter]
        if not word_list_tree.letters:
            return ''.join(word)
    
def get_sentence(letter_counts = letter_counts_example, sentence_tree = sentence_tree_d, word_trees = word_trees_d):
    saved_words = []
    sen = sentences[sentence_counters.index(select_word_using_most_common_letters(sentence_tree, letter_counts))].split(' ')
    for i in range(len(sen)):
        if sen[i].lower() in word_replacement_dict:
            sen[i] = select_word_using_most_common_letters(word_trees[sen[i].lower()], letter_counts)
            saved_words.append(sen[i])
    saved_words_tree = make_full_tree(saved_words)
    best_saved_word = select_word_using_most_common_letters(saved_words_tree, letter_counts)
    sen.append('\n')
    sen.extend(([best_saved_word] *5))
    sen.append('\n'*2)
    return ' '.join(sen)

def main():
    # print(letter_counts_example)
    new_letter_counts_example = {i: random.randint(1, 30) for i in string.ascii_lowercase + ' '}
    new_letter_counts_example['s'] = 100
    print(new_letter_counts_example)
    for i in range(test_generation_amount):
        print(new_letter_counts_example)
        print(get_sentence(new_letter_counts_example))
        

if __name__ == '__main__':
    main()