#!/usr/bin/env python
import sys, getopt
import os
import re


class Fileparser:
    
    '''
        Text file parsing file which converts from spaces to tabs and vice-versa; takes in arguments to specify the conversion procedure
        Program is ran as a module : '-m file_parser'
        Program takes parameters:
            
            -f (--from): defines if the conversion takes place from 'tabs' or 'spaces'
            -r (--replace): if any value given; the changes will be written into the file (if not then copy of the file will be made and changes written into copy)
            -t (--tab-chars): defines how many spaces will replace a tab-to-spaces conversion (default is 4)
            If -f is not given then program will identify if file is seperated by spaces or tabs and ignores other parameters
            Example: -m file_parser -f tabs -r -t 2 
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

    def from_given(self, from_atr, tab_chars_atr, poem_line):
        ret_line = ''
        if from_atr == "tabs":
            if tab_chars_atr == '':
                no_of_spaces = (' '*4)
                ret_line = poem_line.replace('\t', no_of_spaces)
            else :
                no_of_spaces = (' '* int(tab_chars_atr))
                ret_line = poem_line.replace('\t', (no_of_spaces))
        elif from_atr == "spaces":
            ret_line = re.sub(' +', '\t', poem_line)
        return ret_line

    def from_not_given(self, poem_content):
        ret = [0,0]
        for each_line in poem_content:
            for each_letter in each_line:
                if each_letter == " ":
                    ret[0]+=1
                elif each_letter == "\t":
                    ret[1] +=1
        return ret

    def update_count_of_modified_poems(self):
        modified_poems_count_file = open("no_of_modified_poems.txt", "r")
        current_count = (modified_poems_count_file.readline())
        current_count = int(current_count) + 1
        with open("no_of_modified_poems.txt", "w") as modified_poems_count_file:
            modified_poems_count_file.writelines(str(current_count))       
        return current_count

if __name__ == "__main__":
    fp = Fileparser()
    user_args = fp.get_args(sys.argv[1:]) 
    file_name = "poem"
    file_ext = ".txt"
    poem_file = open(file_name + file_ext , "r")
    poem_content = poem_file.readlines()

    if user_args[0] == '' :
        spaces_and_tabs = fp.from_not_given(poem_content)

        if spaces_and_tabs[0] > spaces_and_tabs[1] :
            print("File is fully or mostly seperated by spaces")
        else :
            print("File is fully or mostly seperated by tabs")   
    else :
        line_count = 0
        for each_line in poem_content:
            changed_content = fp.from_given(user_args[0], user_args[2], each_line)
            poem_content[line_count] = changed_content
            line_count+=1
        if user_args[1]:
            with open(file_name+file_ext, "w") as changed_file :
                changed_file.writelines(poem_content)
            print("Total Number of modified poems: %d"  % (fp.update_count_of_modified_poems()))
        else :
            file_name = file_name +"copy"
            current_version = 1
            while os.path.isfile(file_name +str(current_version) + file_ext) or current_version == 100:
                current_version+=1
            file_name = file_name + str(current_version)
            new_file = open(file_name + file_ext, "x")
            for each_line in poem_content:
                new_file.writelines(str(each_line))

            print("Total Number of modified poems: %d" % (fp.update_count_of_modified_poems()))