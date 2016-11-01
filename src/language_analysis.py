#!/usr/bin/python
import re
import inflect
import hyphenator
# from nltk.corpus import cmudict

# d = cmudict.dict() #probably will need this
p = inflect.engine()

#this takes a word and separates its syllables so that they are hyphenated
#also capitalized
def hyphenate_word(word):
	return '-'.join(hyphenator.hyphenate_word(word))

#returns a hyphenated version
def hyphenate_phrase(phrase):
	words = phrase.split(" ")
	returnme = []
	for word in words:
		returnme.append(hyphenate_word(word))
	print(" ".join(returnme))

def word_syllable_count(word):
	return hyphenate_word(word).count('-') + 1

def phrase_syllable_count(phrase):
	if phrase.strip() in ['']:
		return 0
	total = 0
	for word in phrase.split(" "):
		total = total + word_syllable_count(word)
	return total


#takes a really long string and then returns a list of its phrases, also converts numbers
def phrase_break(gan): #gan is an acroym for "Good Argument Name"
	phrases = []
	phrase_finder = "\n+"
	number_finder = "[0-9]+"

	#the next three lines of code work, don't touch them unless they no longer work
	numbers_found = re.findall(number_finder,gan)
	for number in numbers_found:
		gan = gan.replace(number,p.number_to_words(number),1)
	#	yes i did it
	#yatta
	#numbers get changed into words

	#aaron reminder http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
	#make sure the shit gets ruined

	phrases = gan.lower().split("\n")#when the PLEASE TEST IT is above it's referring to make sure this stuff works
	#for i in range(phrases.count('')):
	#	phrases.remove('')
	return phrases

#takes in a word (hyphenated or unhyphenated)
#returns the same word in hypehnated form with info about syllable stress
#example io
#discriminate
#0dis-1crim-0i-2nate
#the number is put before the 
#when it comes to stressing and a syllable (1=primary, 2=secondary, 0=no stress)
def word_syllable_stresser(word):
	stress_amount = ''.join(d[w][0])
	stress_amount = ''.join(i for i in stress_amount if i.isdigit())
	stressed_word = ''
	word = word.split('-')
	for i in range(len(stress_amount)):
		stressed_word = "{}{}".format(stressed_word,"{}{}{}".format(stress_amount[i],word[i],'-'))
		stressed_word = heck[:-1]
	return stressed_word


"""
#does everything
#takes the phrase broken lyrics
#WHAT DOES IT DOOOOO?
def super_anal(gan): #see above for why gan is a good argument name
	pass#@todo(aaron) implement this

#takes in two words and detects if they rhyme,
def detect_word_rhyme(word1, word2):
	words = [word1,word2]
	#@todo(aaron) implement this
'''
language analysis for nightingale
https://github.com/mjlitz/nightingale is the main branch

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
'''"""