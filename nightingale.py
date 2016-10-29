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

#        u1  u2  d2  u3   d3   u4   d4   u5   d5   u6   d6
prob = [0.1,0.45,0.8,0.85,0.90,0.93,0.96,0.97,0.98,0.99,1.00]
f = open('out.txt','w')
f.write('X: 1\nT: Nightingale #1\n')
f.write('M: 4/4\nL: 1/4\nK: C\n')

measure = 0
length = 100
##current note
current = 4
for measure in range(0,10):
  n = random.random()
  i = 0
  while(i<len(prob)):
    if n<=prob[i]:
      added = int(math.ceil(i/2.0))
      if i % 2 == 0:
        added *= -1
      current += added
      #f.write('i = '+str(i)+'\n')
      #f.write('current = '+str(current)+'\n')
      #f.write('added = '+str(added)+'\n')
      #f.write(str(n)+'\n')
      f.write(r[current])
      break  
    i += 1
  measure+= 1

f.close()

#def phrase():

