"""
This module contains the functions to read the fasta file and extract organism.
@Author: Sahi Gonsangbeu
@Date: 2024-02-26
"""


def read_file(filename: str) -> list:
    """Return a list containing the lines of the file.

    Parameters
    ----------
    filename : str
        the file name.
    Returns
    -------
    list
        a list containing the lines of the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()


def extract_organism(lines_list: list) -> str:
    """Extract the organism from the list of lines.

    Parameters
    ----------
    lines_list : list
        the list of lines.
    Returns
    -------
    str
        the organism.
    """
    organism = ""
    for line in lines_list:
        if line[:10] == " ORGANISM":
            # we recover the organism from character 12 to the last but one.
            organism = line[12:-1]
    return organism
