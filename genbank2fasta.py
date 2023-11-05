def read_file(filename):
    """Return a list containing the lines of the file"""
    with open(filename, "r") as f:
        return f.readlines()


def extract_organism(lines_list):
    organism = ""
    for line in lines_list:
        if line[:10] == " ORGANISM":
            # we recover the organism from character 12 to the last but one.
            organism = line[12:-1]
    return organism
