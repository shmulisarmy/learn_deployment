from resources.store_sentence_choices import sentences
from resources.word_dictionary import word_replacement_dict
from collections import Counter

class trie:
    def __init__(self):
        self.letters = {}

    def insert(self, word):
        # print(word)
        if word[0] not in self.letters:
            self.letters[word[0]] = trie()

        if len(word) == 1:
            return
        self.letters[word[0]].insert(word[1::])

def make_full_tree(list):
    tree = trie()
    for i in list:
        tree.insert(i)
    
    return tree

sentence_counters = [''.join(j[0] for j in Counter(i.lower().replace(' ', '')).most_common(10)) for i in sentences]