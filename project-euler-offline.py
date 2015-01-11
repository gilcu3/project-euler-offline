#!/usr/bin/env python
'''
project-euler-offline.py
Christopher Su
Checks solutions to Project Euler problems offline.
'''

import os
import json
from pyDes import *

def loadJSON(jsonStr):
    try:
        data = json.loads(jsonStr)
    except ValueError:
        logging.exception("Error parsing %s." % json_file)
        sys.exit(1)
    return data

def main():
    dir = os.path.dirname(__file__)
    txtFile = open(os.path.join(dir, "solutions-encrypted"), "r")
    txtStr = txtFile.read()
    txtFile.close()
    plain_text = triple_des('03b5660c7c16a07b').decrypt(txtStr, padmode=2)
    solutions = loadJSON(plain_text)
    eof = ["exit", "quit", "q", "c"]

    current = raw_input("What problem are you currently working on? ")
    if current.lower() in eof: exit(0)

    while True:
        proposed = raw_input("\nEnter solution: ")
        if proposed.lower() in eof:
            break
        elif proposed == solutions[current]:
            print "Correct!"
            current = raw_input("\nWhat problem are you working on? ")
            if current == "exit":
                break
        else:
            print "Sorry, but the answer you gave appears to be incorrect." 

if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    main()
