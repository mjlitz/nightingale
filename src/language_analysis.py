from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

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

ALRIGHT SO CURRENT PLAN...
get the stuff
break it into phrases in list form
['phrase1','phrase2',['subphrase1','subphrase2'],'phrase4']
figure out syllable stressing
identify nearby phrases (5 apart?) that rhyme
'''