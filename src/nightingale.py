'''NIGHTINGALE version 0.0

...................
..  NIGHTINGALE  ..
...................

Written by Matt Litzsinger, Andrew Huang, and Aaron Thomas
Updated October 30, 2016



'''

import random
import math

#the range of the music that's created
r = ['C,','D,','E,','F,','G,','A,','B,', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'c', 'd', 'e', 'f', 'g']
#the chance of various intervals. Should add to 1.0. [up 2nd, down 2nd, up 3rd, down 3rd...] 
#               tonic med dom
superphrase_start = [0.7,0.98,1.00]
#        1    2nd  3rd  4th  5th  6th   7th   octave
prob = [0.10,0.75,0.95,0.97,0.99,0.997,0.998,1.000]
# data is number of phrases contained within
superphrases = [3]
phrases = [8,5,5]

f = open('data.txt','w')
f.write('X: 1\nT: Nightingale #1\n')
f.write('M: 4/4\nL: 1/4\nK: G\n')

length = 100
pup = 0.55

previous_interval = 0
up = 0 #up = 1, down = 0
	##current note
key = 4
#dfromtonic = 0

f.write(r[key])
current = key

def parse_phrase(phrase, current, key):
	for note in range(0,phrases[phrase]):
		dfromtonic = current-key
		rand = random.random()
## Factors that affect pup and prob
## 1. Current range. If we are low in the range we want to go higher, if higher we want to go lower
## 2. Relation to tonic and where we are in the phrase. If we're in the middle of the phrase, we want
##    to be higher in the range, then settle down to the tonic by the end of the phrase or superphrase.
## 3. If we are doing a lot of the same interval for too long, we want to do something else. Decrease the
##    probability of an interval after you repeat. Then reset back to default.
		pup = (20-current)/20.0
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
				break  
			else:
				i += 1
#    note+= 1
  

def parse_superphrase(superphrase, current, key):
	phrase = 0
	while (phrase < superphrases[superphrase]):
		parse_phrase(phrase, current, key)
		f.write('|')
		phrase += 1

parse_superphrase(0, current, key)


f.close()

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


	

