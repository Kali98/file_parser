# file_parser
Text file parsing file which converts from spaces to tabs and vice-versa; takes in arguments to specify the conversion procedure:

Program is ran as a module : '-m file_parser'
Program takes parameters:
    -f (--from): defines if the conversion takes place from 'tabs' or 'spaces'
    -r (--replace): if any value given; the changes will be written into the file (if not then copy of the file will be made and changes written into copy)
    -t (--tab-chars): defines how many spaces will replace a tab-to-spaces conversion (default is 4)
    If -f is not given then program will identify if file is seperated by spaces or tabs and ignores other parameters
    Example: -m file_parser -f tabs -r -t 2 