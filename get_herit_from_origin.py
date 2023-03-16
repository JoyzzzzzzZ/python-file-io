#! /usr/bin/env python3

"A module to spot all the locations of herit-derived words from a file."

import re

pattern_str=r'\w*herit\w*'
pattern=re.compile(pattern_str, re.IGNORECASE)

def find_str():
    """
    Read line by line from the file origin.txt. If a line contains a word(s) that matches the given Regex pattern, print the line number and the matched word to the output file. If a line contains more than one hit, every hit is written as a separate line.
    """
    with open('origin.txt','r') as rf:
        with open('herit_out.txt','w') as wf:
            data=rf.readlines()
            nol=len(data)
            rf.seek(0)
            i=1
            while i <= nol:
                line=rf.readline()
                if pattern.search(line) != None:
                    line=re.sub(r'[^\w\s-]', '', line)
                    word_list=line.split(' ')
                    word_target=pattern.findall(line)
                    for word in word_target:
                        wf.write(f"{i}\t{word}\n")
                i += 1

def main():
    find_str()

if __name__ == '__main__':
    main()
