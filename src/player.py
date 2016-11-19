#!/usr/bin/python
import wave
from pygame import mixer
import time
mixer.init()
#takes in abc and wavifies it
#abc is a tuple in abc notation that has data this is meant to process
#name will be the name of the file
def abc_wavify(abc,name):
	pse.make_wav(abc,"~/Music/nightingale/{}.wav".format(name))

#if this works then it means YEE
def play_wav(filepath):
	s = mixer.Sound(filepath)
	s.play()
	time.sleep(s.get_length())

play_wav("out.wav")