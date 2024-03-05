install:
	python -m pip install --upgrade pip
	python -m pip install pylint

run:
	python main.py data/english-common-words.txt data/human-proteome.fasta.txt data/NC_001133.gbk

lint:
	python -m pylint src