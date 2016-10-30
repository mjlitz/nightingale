#!/usr/bin/python
import re
import inflect
import hyphenator

p = inflect.engine()

#def determine_stressed

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
	total = 0
	for word in phrase.split(" "):
		total = total + word_syllable_count(word)
	return total


#takes a really long string and then returns a list. every element in the list
def phrase_break(gan): #gan is an acroym for "Good Argument Name"
	phrases = []
	phrase_finder = "\n+" #@todo(aaron) test this PLEASE TEST IT
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
#	for i in range(phrases.count('')):
#		phrases.remove('')
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