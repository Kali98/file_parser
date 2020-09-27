import unittest
from file_parser import Fileparser


class TestFileParser(unittest.TestCase) :

    #Testing providing all parameterss
    def test_get_argv_all_attr_given(self) :
        fp = Fileparser()
        input_param = ['-f', 'tabs', '-r-', '-t', '1']
        exp_result = ['tabs', True, '1']
        result = fp.get_args(input_param)
        self.assertEqual(result, exp_result)

    #Testing providing everything but no -r-
    def test_get_argv_no_r_given(self) :
        fp = Fileparser()
        input_param = ['-f', 'tabs', '-t', '5']
        exp_result = ['tabs', False, '5']
        result = fp.get_args(input_param)
        self.assertEqual(result, exp_result)
        
    #Testing Providing everything but no -f
    def test_get_argv_no_f_given(self) :
        fp = Fileparser()
        input_param = ['-r-' '-t', '1']
        exp_result = ['', True, '']
        result = fp.get_args(input_param)
        self.assertEqual(result, exp_result)

    #Testing replacing from tabs to 2 spaces
    def test_from_given_tabs_to_spaces(self):
        fp = Fileparser()
        from_atr_val = 'tabs'
        tab_chars_atr_val = '2'
        poem_atr_val = 'To\tbe,\tor\tnot\tto\tbe,\tthat\tis\tthe\tquestion:'
        result = fp.from_given(from_atr_val, tab_chars_atr_val, poem_atr_val)
        self.assertEqual(result, "To  be,  or  not  to  be,  that  is  the  question:")

    #Testing replacing 1 or more spaces to tabs
    def test_from_given_spaces_to_tabs(self):
        fp = Fileparser()
        from_atr_val = 'spaces'
        tab_chars_atr_val = ''
        poem_atr_val = 'To be,  or   not to  be,   that  is the  question:'
        result = fp.from_given(from_atr_val, tab_chars_atr_val, poem_atr_val)
        self.assertEqual(result, "To\tbe,\tor\tnot\tto\tbe,\tthat\tis\tthe\tquestion:")

    #Testing replacing tabs tp spaces with no -t given
    def test_from_given_some_tabs_to_spaces_default_tab_chars(self):
        fp = Fileparser()
        from_atr_val = 'tabs'
        tab_chars_atr_val = ''
        poem_atr_val = 'To be, or\tnot to\tbe, that\tis the\tquestion:'
        result = fp.from_given(from_atr_val, tab_chars_atr_val, poem_atr_val)
        self.assertEqual(result, "To be, or    not to    be, that    is the    question:")

    #Testing output with no f given where poem is 'tab seprerated'
    def test_from_not_given_tab_file(self):
        fp = Fileparser()
        poem_atr_val = 'To\tbe,\tor\tnot\tto\tbe,\tthat\tis\tthe\tquestion:'
        result = fp.from_not_given(poem_atr_val)
        self.assertEqual(result, [0,9])

    #Testing output with no f given where poem is 'space seperated'
    def test_from_not_given_space_file(self):
        fp = Fileparser()
        poem_atr_val = 'To be, or not to be, that is the question:'
        result = fp.from_not_given(poem_atr_val)
        self.assertEqual(result, [9,0])
