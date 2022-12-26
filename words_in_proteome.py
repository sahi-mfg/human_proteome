#!/usr/bin/python3

import argparse


def read_words(filename):
    """
    read the words contained in the file and return a list of the words converted to uppercase and containing 3
    characters or more
    """

    with open(filename) as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            if len(line) >= 3:
                line = line.replace("\n", "")
                new_lines.append(line.upper())
        return new_lines


def read_sequences(filename):
    """
    read the proteome in the file and return a dictionary containing the protein sequences
    """
    with open(filename, "r") as fasta:
        sequence_dict = {}
        for line in fasta:
            if line.startswith(">sp"):
                line = line.lstrip(">sp")
                line = line.lstrip(" ")
                tab = line.split("|")
                protein_id = tab[1]
                line = line.rstrip(" ")
                sequence_dict[protein_id] = ""
            else:
                line = line.rstrip("\n")
                sequence_dict[protein_id] += line
        return sequence_dict


def search_word_in_proteome(seq_dico, word_list):
    """
    Search and counts words in proteome sequences.
    """

    found_word_dict = {}
    for word in word_list:
        seq_count = 0
        for protein_id in seq_dico:
            if word in seq_dico[protein_id]:
                seq_count += 1
        if seq_count != 0:
            found_word_dict[word] = seq_count
            print("{} found {} in sequences".format(word, seq_count))
    return found_word_dict


def find_most_frequent_word(freq_dict):
    """
    Find and print the most frequent word found in the sequences.
    """
    maxi = max(freq_dict.values())
    for word in freq_dict:
        if freq_dict[word] == maxi:
            print("=> {} found in {} sequences".format(word, maxi))
            # print("=> {} found {} times".format(word, maxi))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", default=None)
    parser.add_argument("source_file2", default=None)
    args = parser.parse_args()
    s_file = args.source_file
    s_file2 = args.source_file2
    common_words = read_words(s_file)
    sequences = read_sequences(s_file2)
    found_word = search_word_in_proteome(sequences, common_words)
    find_most_frequent_word(found_word)


if __name__ == "__main__":
    main()
