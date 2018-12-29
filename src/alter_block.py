#!/usr/bin/python
from get_path import *
import sys

def alter_block(path):
    """
    Takes a path to an input file, and outputs a modified text block in the
    current directory.
    """
    
    filepath = str(path)
    output = open('output.txt', 'w')
    searchstr = "<!-- insert features -->"
    with open(filepath) as file:
        line = file.readline()
        while line:
            output.write(line)
            if line.strip() == searchstr:
                output.write("> ***Fey Ancestry***. The acolyte has advantage on saving throws against being charmed, and magic can't put you to sleep.\n")
                output.write(">\n")
            line = file.readline()
    file.close()
    output.close()

if __name__ == "__main__":
    alter_block(get_path(sys.argv[1]))
