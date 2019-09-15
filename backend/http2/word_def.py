import requests
import json
import random
from datamuse import datamuse
dm = datamuse.Datamuse()

# we will be using requests to query the unofficial Google Dictionary API
# from https://googledictionaryapi.eu-gb.mybluemix.net/

class Enlightenmint:

    def __init__(self, learn_words=set()):
        """
        Creates a new Enlightenment object, which can return
        definitions for words and other dictionary operations,
        and will record what words the user is learning

        learn_words: set, the set of initial words the user will learn.
            by default is an empty set
        """
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
        # we check if the word submitted is a real word, ie if a webpage
        # was returned for it. If the word doesn't exist, a HTTP 404 would be returned:
        if(r.status_code==404):
            print("The word "+word+" is either invalid or does not have an entry")
            return "The word "+word+" is either invalid or does not have an entry"
        else:
            ret = []
            # if it's a real word, we add it and return the data:
            self.learn_words.add(word)
            lemmas = json.loads(r.text)
            # count the number of distinct uses of the word
            c=0
            for lemma in lemmas:
                meaning = lemma['meaning']
                for pos in meaning.keys():
                    c+=len(meaning[pos])
            print("Found "+str(c)+" distinct usage(s) of "+"\""+word+"\":")
            ret.append("Found "+str(c)+" distinct usage(s) of "+"\""+word+"\":\n")
            for i, lemma in enumerate(lemmas,1): # for each basic form of the word, eg 'China' and 'china'
                print("Lemma "+str(i)+":")
                ret.append("Based on Root "+str(i)+":\n")
                meaning = lemma['meaning']
                for pos in meaning.keys(): # for each part of speech of the one form of the word, eg 'object' as a noun or verb
                    for usage in meaning[pos]: # for each usage of that word in that pos, eg 'object(n)' as 'an aim' or 'a material thing'
                        definition = usage['definition']
                        print(" "*4+pos)
                        ret.append(" "*4+pos+"\n")
                        print(" "*8+"definition: "+definition)
                        ret.append(" "*8+"definition: "+definition+"\n")
                        if 'example' in usage:
                            print(" "*8+"example of use:")
                            ret.append(" "*8+"example of use:" + "\n")
                            print(" "*12+usage['example'])
                            ret.append(" "*12+usage['example']+"\n")
                        if 'synonyms' in usage:
                            print(" "*8+"synonyms of this use:")
                            ret.append(" "*8+"synonyms of this use:\n")
                            print(" "*12+str(usage['synonyms']))
                            ret.append(" "*12+str(usage['synonyms'])+"\n")
            return ret

    def add_vocab(self, word: str, lang: str='en'):
        """
        Add a word to the set of words to be learned, if it is a real word.
        word: str, the word to be added. If it is not a real word or the set
            learn_words already contains that word, nothing happens
        lang: str, the language of the word to be added. Defaults to English.
        """
        r = requests.get('https://mydictionaryapi.appspot.com', params={'define': word, 'lang': lang})
        if(r.status_code==404):
            return "The word "+word+" is either invalid or does not have an entry"
        else:
            self.learn_words.add(word)

    def remove_vocab(self, word: str):
        """
        Remove a word from the words to be learned, if it exists
        word: str, the word to be removed. If the set learn_words
            does not contain word, nothing happens.
        """
        self.learn_words.discard(word)

    def find_vocab(self):
        """
        Expand the vocab of words to learn by a single commensurate word,
        where commensurate is evaluated on the criteria of being either
        related to words the user is currently learning, and of the word
        being equally obscure (=same likelihood they don't know it)
        """
        # select a random word in the vocab
        vocab = list(self.learn_words)
        i = random.randrange(len(vocab))
        word = vocab[i]
        a = dm.words(rel_bga=word, md='d,f', max=100)
        b = dm.words(rel_bgb=word, md='d,f', max=100)



    def get_vocab(self):
        """
        Return a list of the vocab words the user is currently learning.

        return: list of str, the vocab words the user is currently learning.
        """
        return list(self.learn_words)

    def load_user(self, filepath: str):
        """
        Load the vocabulary of a certain user from the provided .json file,
        setting the learn_vocab list to the words associated with that user.
        Overwrites the current learn_vocab list.
        filepath: str, a filepath to the .json to be loaded.
        """
        with open(filepath) as json_file:
            data=json.load(json_file)
            self.learn_words=set(data)

    def save_user(self, filename: str):
        """
        Save the current vocabulary list learn_vocab into a .json in the users folder
        named after the provided file name.
        filename: str, the filename of the .json to be saved in the users folder
        """
        with open('users/'+filename+'.json', 'w') as outfile:
            json.dump(list(self.learn_words), outfile)

# test stuff below

e = Enlightenmint()
e.define('moiety')
""" e.define('saw')
e.define('wack')
e.define('inexorable')
e.remove_vocab('wick')
e.add_vocab('blahsdf')
e.remove_vocab('saw')
e.save_user('eris')

print(e.get_vocab())
e.load_user('users/sator.json')
print(e.get_vocab()) """


#r = requests.get('https://mydictionaryapi.appspot.com', params={'define': 'lsw', 'lang': 'en'})
#print(r.status_code)
#lemmas = json.loads(r.text)
#print('ccc')
#print(r)
#print(lemmas)
#e.define('bind')
