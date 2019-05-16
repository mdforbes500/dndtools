#!/usr/bin/python

import sqlite3
import sys

def get_path(template):
    """Returns path for the stat block for an NPC from the NPC template database
    based upon the name passed by parameter."""

    conn = sqlite3.connect('../databases/npctemplates')

    cursor = conn.execute("""
    SELECT PATH FROM templates
    WHERE NAME LIKE ?
    """, ('%'+ str(template) +'%',))

    for row in cursor:
        paths = row[0]

    conn.close()
    return paths

if __name__ == "__main__":
    get_path(sys.argv[1])
