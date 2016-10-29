#!/usr/bin/python2
'''
from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9001') #it's over NINE THOUSAND!
i might not use this
'''
from nltk.corpus import cmudict

d = cmudict.dict()

def hyphenate_phrase(word):
	return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
#this is from http://stackoverflow.com/a/4103234
#thank you internet stranger for writing code that does what I want
#i renamed the function to hyphenate_phrase 


#takes a really long string and then returns a list. every element in the list
def phrase_break(gan): #gan is an acroym for "Good Argument Name"
	phrases = []

	while len(phrases) > 0:
		current_phrase = ''
		next_index = '//todo(aaron) WRITE CODE TO DO THIS'#find beginning of next phrase, save its location in next_index
		current phrase = gan[:next_index]

		#set cuttent_phrase to be a substring of 0 to the next beginning
		#add it to phrases
		#remove the current_phrase from gan
		eocp = gen.rfind(current_phrase) #end of current phrase
		gan = gan[eocp:]
		#these two lines of code might be redundant (in a bad way)
		#gan = gan[next_index:] #I THINK THIS LINE DOES WHAT THE ABOVE TWO DO
	return phrases

#takes a really long string, breaks it into phrases, and then hyphenates the phrases
	def break_and_hyphenate(gan):
		phrases = phrase_break(gan)
		for phrase in phrases:
			phrase = hyphenate_phrase(phrase)
'''
language analysis for nightingale
https://github.com/mjlitz/nightingale is the main branch
i'm commiting to https://github.com/metruption/nightingale
it works, but could be better ¯\_(ツ)_/¯

things that i need this code to do
identify rhymes (end of line and internal rhyming)
determine which syllables are stressed (do this before rhyme stuff)

pseudocode of this
isolate the phrases
identiy rhymes at ends of phrases
find most important word in each sentence

ALRIGHT SO CURRENT PLAN...
get the stuff
break it into phrases in list form
['phrase1','phrase2',['subphrase1','subphrase2'],'phrase4']
figure out syllable stressing
identify nearby phrases (5 apart?) that rhyme
'''