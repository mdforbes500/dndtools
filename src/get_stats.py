#!/usr/bin/python

import sqlite3
import sys

def get_stats(template):
    """Finds the stat block for an NPC from the NPC template provided by the
    user."""

    conn = sqlite3.connect('../databases/npctemplates')

    cursor = conn.execute("""
    SELECT ID, NAME, PATH, EQUIVALENT FROM templates
    WHERE NAME LIKE ?
    """, ('%'+ str(template) +'%',))

    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PATH = ", row[2])
        print("EQUIVALENT = ", row[3], "\n")

    conn.close()

if __name__ == "__main__":
    get_stats(sys.argv[1])
