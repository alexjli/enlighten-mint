import requests
import json
from datamuse import datamuse
dm = datamuse.Datamuse()

# we will be using requests to query the unofficial Google Dictionary API 
# from https://googledictionaryapi.eu-gb.mybluemix.net/

class Enlightenmint:

    def __init__(self, learn_words=[]):
        self.learn_words = learn_words

    def define(self, word: str, lang: str='en'):
        """
        Defines a given word with its Definition, an Example usage, 
        and provides Related words to it.
        Records that the user has requested a definition of this word.

        word: str, the word to be defined
        lang: str, a language code for the language the word 
            is being searched in (default English, or 'en')
        return: the text definition of a word with example usages and related words
        """
        self.learn_words.append(word)

        # the Google Dictionary API will return a text string which is 
        # formatted in a very specific way:
        # it is an array that contains dictionaries (I call them 'lemmas')
        # corresponding to basic forms of the word, eg 'China' and 'china'.
        # each dict lemma hashes 'meaning' to a dictionary of parts of speech (pos) 
        # of that usage, eg 'noun' and 'verb' for the lemma 'object'
        # each pos is hashed to an array of dictionaries, 
        # each dictionary representing a separate usage, 
        # eg 'object' as 'an aim' and 'a material thing'
        r = requests.get('https://mydictionaryapi.appspot.com', params={'define': word, 'lang': lang})
        lemmas = json.loads(r.text)
        
        # count the number of distinct uses of the word
        c=0
        for lemma in lemmas:
            meaning = lemma['meaning']
            for pos in meaning.keys():
                c+=len(meaning[pos])
        print("Found "+str(c)+" distinct usages of "+"\""+word+"\":")
        for i, lemma in enumerate(lemmas,1): # for each basic form of the word, eg 'China' and 'china'
            print("Lemma "+str(i)+":")
            meaning = lemma['meaning']
            for pos in meaning.keys(): # for each part of speech of the one form of the word, eg 'object' as a noun or verb
                for usage in meaning[pos]: # for each usage of that word in that pos, eg 'object(n)' as 'an aim' or 'a material thing'
                    definition = usage['definition']
                    print(" "*4+pos)
                    print(" "*8+"definition: "+definition)
                    if 'example' in usage:
                        print(" "*8+"example of use:")
                        print(" "*12+usage['example'])
                    if 'synonyms' in usage:
                        print(" "*8+"synonyms of this use:")
                        print(" "*12+str(usage['synonyms']))


e = Enlightenmint()
e.define('object')