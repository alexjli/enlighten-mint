#from nltk.corpus import words
#print('fine' in words.words())

"""from nltk.corpus import words
from datamuse import datamuse
dm = datamuse.Datamuse()

def define_word(word, n=3):
    
    Define a given word by showing a number of words with similar meaning.

    word: the word to be defined
    n: the number of synonyms to generate
    return: a list of these words
    
    return(dm.words(ml=word, md='d', max=n))

print(define_word('food'))
print('food' in words.words())"""

#from datamuse import datamuse
#dm = datamuse.Datamuse()
#orange_rhymes = dm.words(rel_rhy='orange', max=5)
#print(orange_rhymes)

#import requests
#import re
#import xml
#r = requests.get('http://en.wiktionary.org/w/index.php?title=test&printable=yes')
#c = requests.get('http://en.wiktionary.org/w/index.php', params={'title': 'test', 'printable': 'yes'})
#print(r.text)


import requests
# we will be using requests to query the unofficial Google Dictionary API 
# from https://googledictionaryapi.eu-gb.mybluemix.net/

r = requests.get('https://mydictionaryapi.appspot.com', params={'define': 'test'})
print(r.text["meaning"])

