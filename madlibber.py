#! python3
# madlibber.py - Reads a file mad lib.
#  The user is prompted to fill in the
#  appropriate words. The program will print the finished
#  mad lib at the end and save it to a new file.
# Usage: madlibber <path> -runs the mablibber.py program
#  and searches <path> for mad lib text files. Then prompts
#  user to enter appropriate words to fill in blanks,
#  creating a new text file with filled in madlib.

import pyperclip,re,sys,os,shelve

adj_regex = re.compile(r'ADJECTIVE')
noun_regex = re.compile(r'NOUN')
verb_regex = re.compile(r'VERB')

# madlib_shelf = shelve.open('madlib')
# Create new finishedmadlib%s file copy of madlib.txt
finished_madlib = open("finished_madlib", 'w')

# Read command line and find madlib.txt at <abs path>
if len(sys.argv) == 2:
    madlib_file = open(sys.argv[1], 'r')
    madlib_file_contents = madlib_file.readlines()
    
    # Detect ADJECTIVE, NOUN, VERB in the file.
    for line in madlib_file_contents:
        adjectives = adj_regex.findall(line)
        nouns = noun_regex.findall(line)
        verbs = verb_regex.findall(line)
    print('adjectives are: ' + str(adjectives))
    print('nouns are: ' + str(nouns))
    print('verbs are: ' + str(verbs))
# TODO: For each ADJECTIVE, NOUN, or VERB, ask user input

# TODO: Store input into variable and replace ADJ, N, OR V

# Close new file and print contents to screen.
madlib_file.close()

