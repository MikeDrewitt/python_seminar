#!/usr/bin/python

import sys, traceback

import PS4_Test_Suite as PS4

'''
A Python testing suite that calls testing functions. Those functions are expected to return a 
score as an int. Those scores are summed and printed from the run_test_suite method.

    @param total_tests
        The total number of tests to be run. This is what gets looped over and concatenated with the
        question header 

    @param question_header
        The format of the testing functions. This gets concatenated with the current test number,
        the function will then be called. 
            ie: If the function you want called is named Test_Q1(), then your question header would
            be 'Test_Q'.

    @param module
        The module name for the file or object that the testing functions are located.
            ie: If you're running the testing suite from this file and include your testing code via
            
            'import Testing_Code as TC'

            TC would be your module.
'''
class python_tester:
    
    def __init__(self):
        self.score = 0
        self.total_tests = 0
        self.question_header = 'Q'
        self.module = 'default_import'

    def __init__(self, total_tests, question_header, module):
        self.score = 0
        self.total_tests = total_tests
        self.question_header = question_header
        self.module = module
 
    '''
    Converts int 1 to Passed or Failed otherwise
    '''
    def passed_string_conversion(self, pass_fail):
        if pass_fail == 1:
            return 'Passed'
        else:
            return 'Failed'

    '''
    Loops over the total number of testing functions given a standard naming convention between tests,
    and a numberd order of the tests. This expects the testing functions to return an int (aka score)
    and sums those to get a final score. 
    
    This method does print meta information about the running tests, and also edits the information
    of the testing object so as to be used later if needed. 
    '''
    def run_test_suite(self):
        total_questions = 15

        for i in range(1, total_questions + 1):
            test_name = 'run_Q' + str(i)

            print('Running test', i, '...')
            
            
            try:
                current_test = getattr(self.module, test_name)()
            except:
                current_test = 0
                traceback.print_exc(file=sys.stdout)
   
            self.score += current_test
            pass_fail = self.passed_string_conversion(current_test)

            print('\tTest ' + str(i) +': '+ pass_fail)

        print('Total: ' + str(self.score) + '/' + str(total_questions))

if __name__ == "__main__":

    tester = python_tester(15, 'run_Q', PS4)
    tester.run_test_suite()

