#!/usr/bin/python
import re
import inflect
import hyphenator
from nltk.corpus import cmudict

d = cmudict.dict() #probably will need this
p = inflect.engine()

#this takes a word and separates its syllables so that they are hyphenated
#also capitalized
#if it takes a hyphenated word it should just return the hyphenated word (i have implemented this)
def hyphenate_word(word):
	word = '-'.join(hyphenator.hyphenate_word(word))
	if '--' in word:
		word = '-'.join(word.split('--'))
	return word

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
#in current version (v0.1.3-alpha) only breaks up the phrases at line breaks
def phrase_break(gan): #gan is an acroym for "Good Argument Name"
	phrases = []
	phrase_finder = "\n+"
	number_finder = "[0-9]+"

	#changes numberical numbers to written numbers
	numbers_found = re.findall(number_finder,gan)
	for number in numbers_found:
		gan = gan.replace(number,number_to_words(number),1)

	#aaron reminder http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
	#we might need that later, just a reminder for aaron

	phrases = gan.lower().split("\n")
	#for i in range(phrases.count('')): #this removes all blank lines
	#	phrases.remove('')				#what if each stanza was a sub-list and then we detect identical stanzas
	return phrases

#takes in a word (hyphenated or unhyphenated)
#returns the same word in hypehnated form with info about syllable stress
#example io
#discriminate
#0dis-1crim-0i-2nate
#the number is put before the
#when it comes to stressing and a syllable (1=primary, 2=secondary, 0=no stress)
def word_syllable_stresser(word):
	stress_amount = ''.join(d[word][0])
	stress_amount = ''.join(i for i in stress_amount if i.isdigit())
	stressed_word = ''
	word = word.split('-')
	for i in range(len(stress_amount)):
		stressed_word = "{}{}".format(stressed_word,"{}{}{}".format(stress_amount[i],word[i],'-'))
		# stressed_word = heck[:-1] not sure what this was for, if you see this comment after august 26, 2018 just delete it
	return stressed_word


#returns the last syllable of a word (hypehnated or unphypehnated)
def word_last_syl(word):
	word = la.hyphenate_word(word)
	while '-' in word:
		word = word[word.index('-')+1:]
	return word


#takes in two words and detects if they rhyme,
def detect_word_rhyme(word1, word2):
	pass



#does everything
#takes the phrase broken lyrics
#WHAT DOES IT DOOOOO?
def super_analysis(gan): #see above for why gan is a good argument name
	pass#@todo(aaron) implement this
