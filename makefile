all: inflect pysynth pygame nltk

python3:
	#@sudo apt-get update; \
	sudo apt-get install python3

inflect:
	pip install -e git+https://github.com/pwdyson/inflect.py#egg=inflect

pysynth:
	mkdir PySynth; \
	git clone https://github.com/mdoege/PySynth PySynth; \
	cd PySynth; \
	sudo python3 setup.py install; \
	cd ..

pygame:
	pip install pygame --user

nltk:
	sudo pip install -U nltk; \
	sudo pip install -U numpy; \
	sudo apt autoremove