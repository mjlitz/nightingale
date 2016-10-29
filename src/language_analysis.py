#!/usr/bin/python2
'''
from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9001') #it's over NINE THOUSAND!
i might not use this
'''
from nltk.corpus import cmudict
import re
import inflect

d = cmudict.dict()
p = inflect.engine()
#p.number_to_words(99) returns "ninety-nine"

def word_syllable_count(word):
	return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
#this is from http://stackoverflow.com/a/4103234
#thank you internet stranger for writing code that does what I want
#i renamed the function to word_syllable_count

def phrase_syllable_count(phrase):
	total = 0
	for word in phrase.split(" "):
		total = total + word_syllable_count(word)
	return total

#this takes a word and separates its syllables so that they are hyphenated
#also capitalized
def hyphenate_word(word):
	pass #//@todo(aaron) write this

#returns a hyphenated version
def hyphenate_phrase(phrase):
	words = phrase.split()
	for word in words:
		word = hyphenate_word(word)
	return ''.join(words)

#takes a really long string and then returns a list. every element in the list
def phrase_break(gan): #gan is an acroym for "Good Argument Name"
	phrases = []
	phrase_finder = "//todo(aaron) make this"
	number_finder = "[0-9]+"

	numbers_found = re.findall(number_finder,gan)
	for number in numbers_found:
		gan = gan.replace(number,p.number_to_words(number),1)
	#	yes i did it
	#yatta
	#numbers get changed into words

	"""
	#so this loop might be mostly redundant
	while len(phrases) > 0:
		current_phrase = ''
		next_index = rm.match(phrase_finder,gan)#find beginning of next phrase, save its location in next_index
		current_phrase = gan[:next_index]


		'''
		#we might not want to do this, find a way to process a phrase consisting of two subphrases
		if current_phrase.find(',') != -1:#if a phrase has two subphrases
			current_phrase = current_phrase.split(',')
		'''#yeah i'm not gonna do that for now

		gan = gan[next_index:] #might need to do a +1 or a -1. figure it out once I'm ready to test this function
	
	#more on tha loop being redundant
	'''"""
	phrases = re.split(phrase_finder,gan) #this line of code probably could take that loop's place
	return phrases

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
['phrase1','phrase2','phrase3','phrase4']
figure out syllable stressing
identify nearby phrases (5 apart?) that rhyme
'''