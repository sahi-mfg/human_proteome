# human proteome project

The goal of this mini project is to discover if English words can be found in sequences of the human proteome, i.e. in the sequences of all human proteins.
human proteins.
we have at our disposal:

- The file english-common-words.txt , which contains the 3000 most frequent English words,
at a rate of 1 word per line.

- The human-proteome.fasta file which contains the human proteome in the form of
sequences in FASTA format.

- The NC_001133.gbk file which contains the genome of the yeast Saccharomyces cerevisiae in     GenBank format.

# How to use it

```git clone human-proteome-project```

```cd human-proteome-project```


```python main.py data/english-common-words.txt data/human-proteome.fasta.txt data/NC_001133.gbk```
