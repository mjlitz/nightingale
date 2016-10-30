#!/usr/bin/python
import language_analysis as la
import lyrics

'''
provide matt with a way to print the syllavbles of each line into a phrase
'''

def analyze_lyric(gan):
	phrases = la.phrase_break(gan)
	for phrase in phrases:
		print(la.hyphenate_phrase(phrase))
		print(la.phrase_syllable_count(phrase))
		print('')

print(analyze_lyric(lyrics.rick))