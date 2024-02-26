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
    parser.add_argument("english_common_words", default=None)
    parser.add_argument("proteome_fasta", default=None)
    parser.add_argument("gbk_file", default=None)
    args = parser.parse_args()
    english_common_words = args.english_common_words
    proteome_fasta = args.proteome_fasta
    gbk_file = args.gbk_file
    common_words = read_words(english_common_words)
    sequences = read_sequences(proteome_fasta)
    list_of_lines = read_file(english_common_words)
    print(f"Number of lines read {list_of_lines}:{list_of_lines}")
    name_organism = extract_organism(list_of_lines)
    print("organism :", name_organism)
    found_word = search_word_in_proteome(sequences, common_words)
    find_most_frequent_word(found_word)
