DATA = ./data/*.txt
SRC = *.py

run:
	python main.py

send :
	git add $(SRC) $(DATA) Makefile
	git commit -m "the simulation data can be saved and read in files"
	git push
