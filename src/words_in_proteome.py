""""
This module contains functions to read words from a file and search for them in a proteome.
@Author: Sahi Gonsangbeu
@Date: 2024-02-26
"""


def read_words(filename: str) -> list:
    """Read the words from a file and return a list of words.

    Parameters
    ----------
    filename : str
        The file name.

    Returns
    -------
    list
        list of words.
    """

    with open(filename) as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            if len(line) >= 3:
                line = line.replace("\n", "")
                new_lines.append(line.upper())
        return new_lines


def read_sequences(filename: str) -> dict:
    """Read protein sequences from a fasta file and return a dictionary
    with protein id as key and sequence as value.

    Parameters
    ----------
    filename : str
        the file name.

    Returns
    -------
    dict
        a dictionary with protein id as key and sequence as value.
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


def search_word_in_proteome(seq_dico: dict, word_list: list) -> dict:
    """Search for the words in the sequences and return a dictionary with the words
    as key and the number of sequences containing the word as value.

    Parameters
    ----------
    seq_dico : dict
        the sequence dictionary.
    word_list : list
        the list of words to search.

    Returns
    -------
    dict
        dictionary with the words as key and the number of sequences
        containing the word as value.
    """

    found_word_dict = {}
    for word in word_list:
        seq_count = 0
        for protein_id in seq_dico:
            if word in seq_dico[protein_id]:
                seq_count += 1
        if seq_count != 0:
            found_word_dict[word] = seq_count
            print(f"{word} found {seq_count} in sequences")
    return found_word_dict


def find_most_frequent_word(freq_dict: dict) -> None:
    """Find the most frequent word in the dictionary and print it."""
    maxi = max(freq_dict.values())
    for word in freq_dict:
        if freq_dict[word] == maxi:
            print(f"=> {word} found in {maxi} sequences")
            # print("=> {} found {} times".format(word, maxi))
