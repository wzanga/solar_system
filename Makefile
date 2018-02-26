DATA = ./data/*.txt
SRC = *.py

run:
	python main.py

send :
	git add $(SRC) $(DATA) Makefile
	git commit -m "method to retrieve all the states of each body done"
	git push
