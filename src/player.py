#!/usr/bin/python
import pysynth_e as pse
import wave
import pygame
pygame.init()
#takes in abc and wavifies it
#abc is a tuple in abc notation that has data this is meant to process
#name will be the name of the file
def abc_wavify(abc,name):
	pse.make_wav(abc,fn = "~/Music/nightingale/{}.wav".format(name))

#if this works then it means YEE
def play_wav(filepath):
	s = pygame.mixer.Sound(filepath)
	s.start()
	s.stop()