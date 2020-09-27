#!/usr/bin/env python
import sys, getopt
import os
import re


class Fileparser:
    
    '''
        Program is ran as a module : '-m file_parser'
        Program takes parameters:
            
            -f (--from): defines if the conversion takes place from 'tabs' or 'spaces'
            -r (--replace): if any value given; the changes will be written into the file (if not then copy will be made)
            -t (--tab-chars): defines how many spaces will replace a tab-to-spaces conversion (default is 4)
            If -f is not given then program will identify if file is seperated by spaces or tabs and ignores other parameters

    '''

    def __init__(self, from_val = None, replace_val = None, tab_chars_val = None):
        self.from_val = ''
        self.replace_val = False
        self.tab_chars_val = ''    

    def get_args(self, argv):
        try:
            opts, args = getopt.getopt(argv,"helpf:r:t:",["from=","replace=","tab-chars="])
        except getopt.GetoptError:
            print ('-m file_parser -f <from> -r <replace> -t <tab-chars>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-help':
                print ('-m file_parser -f <from> -r <replace> -t <tab-chars>')
                sys.exit()
            elif opt in ("-f", "--from"):
                self.from_val = arg
            elif opt in ("-r", "--replace") or (opt in " "):
                self.replace_val = True
            elif opt in ("-t", "--tab-chars"):
                self.tab_chars_val = arg
        
        arguments = [self.from_val, self.replace_val, self.tab_chars_val]
        return arguments

    def from_given(self, from_atr, tab_chars_atr, poem_content):
        ret_content = ''
        if from_atr == "tabs":
            if tab_chars_atr == '':
                no_of_spaces = (' '*4)
                ret_content = poem_content.replace('\t', no_of_spaces)
            else :
                no_of_spaces = (' '* int(tab_chars_atr))
                retLine = poem_content.replace('\t', (no_of_spaces))
        elif from_atr == "spaces":
            retLine = re.sub(' +', '\t', poem_content)
        return ret_content

    def from_not_given(self, poem_content):
        ret = [0,0]
        for each_line in poem_content:
            for each_letter in each_line:
                if each_letter == " ":
                    ret[0]+=1
                elif each_letter == "\t":
                    ret[1] +=1
        return ret

if __name__ == "__main__":
    fp = Fileparser()
    user_args = fp.get_args(sys.argv[1:]) 
    print(user_args)