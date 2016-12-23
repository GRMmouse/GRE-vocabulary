import os
from mw import getDefs

PATH = "storage/"

def read(filename, mode="rt"):
    # rt = "read text"
    with open(PATH+filename, mode) as fin:
        return fin.read()

def write(filename, contents, mode="wt"):
    # wt = "write text"
    with open(PATH+filename, mode) as fout:
        fout.write(contents)


def rawToWhole():
    content = read("raw_vocab.txt").splitlines()
    for index in xrange(len(content)):
        word = content[index]
        meaning = "#".join(getDefs(word))
        content[index] = "%s@%s@0"%(word, meaning)
        print content[index]
    content = "\n".join(content)
    write("vocab_with_def.txt", content)
    raw_input("Press enter to quit.")
    return

def wholeToRaw():
    content = read("vocab.txt").splitlines()
    vocabs = map(lambda s: s.split('@')[0], content)
    write("raw_vocab.txt", ('\n'.join(sorted(vocabs))))

rawToWhole()