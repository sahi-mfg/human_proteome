# human proteome project

The goal of this mini project is to discover if English words can be found in sequences of the human proteome, i.e. in
the sequences of all human proteins.
human proteins.
we have at our disposal:

- The file english-common-words.txt , which contains the 3000 most frequent English words,
  at a rate of 1 word per line.

- The human-proteome.fasta file which contains the human proteome in the form of
  sequences in FASTA format.

- The NC_001133.gbk file which contains the genome of the yeast Saccharomyces cerevisiae in GenBank format.

# How to use it

- Clone the repository: `git clone git@github.com:momosahi/human_proteome.git`
  or `git clone https://github.com/momosahi/human_proteome.git`

- `cd human-proteome-project`

- run it using the following
  command: `python main.py data/english-common-words.txt data/human-proteome.fasta.txt data/NC_001133.gbk`

- Or use makefile: `make run`