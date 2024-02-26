"""
Main module for the project.
@Author: Sahi Gonsangbeu
@Date: 2024-02-26
"""

import argparse

from src.genbank2fasta import read_file, extract_organism
from src.words_in_proteome import (
    read_sequences,
    search_word_in_proteome,
    find_most_frequent_word,
    read_words,
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", default=None)
    parser.add_argument("source_file2", default=None)
    parser.add_argument("source_file3", default=None)
    args = parser.parse_args()
    s_file = args.source_file
    s_file2 = args.source_file2
    s_file3 = args.source_file3
    common_words = read_words(s_file)
    sequences = read_sequences(s_file2)
    list_of_lines = read_file(s_file)
    print("Number of lines read {}:{}".format(list_of_lines, len(list_of_lines)))
    name_organism = extract_organism(list_of_lines)
    print("organism :", name_organism)
    found_word = search_word_in_proteome(sequences, common_words)
    find_most_frequent_word(found_word)
