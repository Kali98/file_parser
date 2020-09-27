#!/usr/bin/env python
import sys, getopt
import os
import re


class Fileparser:
    
    '''
        
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

if __name__ == "__main__":
    fp = Fileparser()
    user_args = fp.get_args(sys.argv[1:]) 
    print(user_args)