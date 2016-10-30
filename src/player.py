#!/usr/bin/python
import pysynth_e as pse

#takes in abc and wavifies it
#abc is a tuple in abc notation that has data this is meant to process
#name will be the name of the file
def abc_wavify(abc,name):
	pse.make_wav(abc,fn = "{}.wav".format(name))