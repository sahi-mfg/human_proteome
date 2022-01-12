#!/usr/bin/python3

import argparse


def lit_fichier(filename):
    """" return a list containing the lines of the file """
    with open(filename, 'r') as f:
        return f.readlines()


def extrait_organisme(lines_list):
    organisme = ""
    for line in lines_list:
        if line[:10] == " ORGANISM":
            # on récupère l'organisme du caractère 12 jusqu'à l'avant dernier
            organisme = line[12:-1]
    return organisme


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_file', default=None)
    args = parser.parse_args()
    s_file = args.source_file
    liste_des_lignes = lit_fichier(s_file)
    print("Nombre de lignes lues {}:{}".format(liste_des_lignes, len(liste_des_lignes)))
    nom_organisme = extrait_organisme(liste_des_lignes)
    print("oragnisme :", nom_organisme)


if __name__ == '__main__':
    main()
