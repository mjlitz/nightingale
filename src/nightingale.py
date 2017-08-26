#!/usr/bin/python
'''NIGHTINGALE version 0.1.4

about versioning:
left number increasing means that it will break backwards compatibility
middle number increasing means there's a new feature or something big-ish like that
right number increases basically whenever we feel like the changes are big enough to increase that number

...................
..  NIGHTINGALE  ..
...................

Written by Matt Litzsinger, Aaron Thomas, and Andrew Huang
Created on October 30, 2016 for HacKNC
'''

import random
import math
import language_analysis as la
import lyrics

#the range of the music that's created
r = ['C,','D,','E,','F,','G,','A,','B,', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'c', 'd', 'e', 'f', 'g']
#the chance of various intervals. Should add to 1.0. [up 2nd, down 2nd, up 3rd, down 3rd...] 
#               tonic med dom
superphrase_start = [0.7,0.98,1.00]
#        1    2nd  3rd  4th  5th  6th   7th   octave
prob = [0.10,0.75,0.95,0.97,0.99,0.997,0.998,1.000]
# data is number of phrases contained within

lyric_lines = la.phrase_break(lyrics.song)
syl_count = []
for i in lyric_lines:
	syl_count.append(la.phrase_syllable_count(i))
if syl_count[0] != 0:
	syl_count = [0] + syl_count
syl_count.append(0)
print('len sylcount = '+str(len(syl_count)))
print(syl_count)
syl_pointer = 1

f = open('data.abc','w')
f.write('X: 1\nT: Nightingale #1\n')
f.write('Q: 1/4 = 113\nM: 4/4\nL: 1/8\nK: Bmin\n')

key = 3
length = 100
pup = 0.55

previous_interval = 0
up = 0 #up = 1, down = 0
	##current note
key = 4
#f.write(r[key])
current = key

	

## writes a note length based on which note (1 note = 1 syllable), how many syllables, how many beats used. Writing nothing means default note length.
def decide_length(note,syllables,current_beat):
## we have more notes
	if note < syllables:
		current_beat += 1
		if current_beat % 8 == 0:
			f.write('|')
##no more notes, let's rest
	elif note == syllables:
		current_beat += 1
		if current_beat < 8:
			f.write('z'+str(8-current_beat))
			f.write('|')
			f.write('z8')
		else:
			f.write('z'+str(16-current_beat))
		
	return current_beat
def parse_phrase(phrase, current, key):
	note = 1	##counting from 1
	current_beat = 0 ##divisible by 2, 4 are stress beats
	print (syl_count[phrase])
	while (note <= syl_count[phrase]):
		dfromtonic = current-key
		rand = random.random()
## Factors that affect pup and prob
## 1. Current range. If we are low in the range we want to go higher, if higher we want to go lower
## 2. Relation to tonic and where we are in the phrase. If we're in the middle of the phrase, we want
##    to be higher in the range, then settle down to the tonic by the end of the phrase or superphrase.
## 3. If we are doing a lot of the same interval for too long, we want to do something else. Decrease the
##    probability of an interval after you repeat. Then reset back to default.
		pup = (15-current)/15.0
#		f.write('pup = '+str(pup)+'\n')
		i = 0
		while(i<len(prob)):
			if rand <= prob[i]:
				added = int(math.ceil(i/2.0))
				rand2 = random.random()
				if rand2 > pup:#down interval, subtract added value instead
					added *= -1
				current += added
				#f.write('i = '+str(i)+'\n')
				#f.write('current = '+str(current)+'\n')
				#f.write('added = '+str(added)+'\n')
				#f.write(str(n)+'\n')
				f.write(r[current])
				current_beat = decide_length(note,syl_count[phrase],current_beat)
				break  
			else:
				i += 1
		note += 1
	f.write('|')

def find_block(syl_pointer):
	begin = syl_pointer
	while (syl_count[syl_pointer] != 0):
		syl_pointer += 1
	end = syl_pointer
	block_length = end-begin
	print('block_length = '+str(block_length))
	return block_length


def parse_superphrase(begin, length, current, key):
	phrase = begin
	while (phrase < begin+length):
		parse_phrase(phrase, current, key)
		f.write('\n')
		#f.write('|')
		phrase += 1


## main method
while (syl_pointer < len(syl_count)):
	print('syl_pointer = '+str(syl_pointer))
	begin = syl_pointer
	length = find_block(syl_pointer)
	parse_superphrase(begin, length, current, key)
	syl_pointer += length + 1


f.close()

#development for phrases
'''for phrase in range(0,len(phrases)):
	phrase = 0
	for note in range(0,phrases[phrase]):
		rand = random.random()
		i = 0
		while(i<len(prob)):
			if rand <= prob[i]:
				added = int(math.ceil(i/2.0))
				rand2 = random.random()
				if rand2 > pup:#down interval, subtract added value instead
					added *= -1
				current += added
				dfromtonic += added
        #f.write('i = '+str(i)+'\n')
        #f.write('current = '+str(current)+'\n')
        #f.write('added = '+str(added)+'\n')
        #f.write(str(n)+'\n')
        f.write(r[current])
        break  
      i += 1
    note+= 1
  f.write('|')
  phrase += 1'''


	

