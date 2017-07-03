#!/usr/bin/env python
'''
project-euler-offline.py
Christopher Su
Checks solutions to Project Euler problems offline.
'''

import os
import json
from pyDes import *

key = '03b5660c7c16a07b'

def loadJSON(jsonStr):
    try:
        data = json.loads(jsonStr)
    except ValueError:
        print "Error parsing file."
        sys.exit(1)
    return data

def process_solutions():
    dir = os.path.dirname(__file__)
    txtFile = open(os.path.join(dir, "solutions-plain"), "r")
    data = {}
    for line in txtFile.readlines():
        if len(line.split()) > 1:
            prob = unicode(line.split()[0][:-1])
            sol = unicode(line.split()[1])
            data[prob] = sol
    txtFile.close()

    str = json.dumps(data)

    enc_str = triple_des(key).encrypt(str, padmode=2)
    ff = open('solutions-encrypted-last', 'w')
    ff.write(enc_str)
    ff.close()


def main():
    eof = ["exit", "quit", "q", "c"]
    dir = os.path.dirname(__file__)

    current = raw_input("What problem are you currently working on? ")
    if current.lower() in eof: exit(0)


    proposed = raw_input("Enter solution: ")

    txtFile = open(os.path.join(dir, "solutions-encrypted-last"), "r")
    txtStr = txtFile.read()
    txtFile.close()
    plain_text = triple_des(key).decrypt(txtStr, padmode=2)
    solutions = loadJSON(plain_text)

    if proposed.lower() in eof:
        exit(0)
    elif current not in solutions:
        print 'We dont have the solution for that problem yet :('
    elif proposed == solutions[current]:
        print "Correct!\n"
    else:
        print "Sorry, but the answer you gave appears to be incorrect." 

if __name__ == "__main__":
    #process_solutions()
    main()
