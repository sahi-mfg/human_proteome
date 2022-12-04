#!/usr/bin/python3

import argparse


def read_file(filename):
    """" return a list containing the lines of the file """
    with open(filename, 'r') as f:
        return f.readlines()


def extract_organism(lines_list):
    organism = ""
    for line in lines_list:
        if line[:10] == " ORGANISM":
            # we recover the organism from character 12 to the last but one.
            organism = line[12:-1]
    return organism


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', default=None)
    args = parser.parse_args()
    s_file = args.source_file
    list_of_lines = read_file(s_file)
    print("Number of lines read {}:{}".format(list_of_lines, len(list_of_lines)))
    name_organism = extract_organism(liste_des_lignes)
    print("organism :", name_organism)


if __name__ == '__main__':
    main()
