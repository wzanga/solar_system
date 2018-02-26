DATA = ./data/*.txt
SRC = *.py

run:
	python main.py

send :
	git add $(SRC) $(DATA) Makefile
	git commit -m "add add different integration methods"
	git push
