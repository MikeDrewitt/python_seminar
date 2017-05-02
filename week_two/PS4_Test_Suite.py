#!/usr/bin/python

import sys, traceback

try:
    import PS4_Solutions as student_file
except:
    print('You have at least one syntax error ...')
    traceback.print_exc(file=sys.stdout)
    sys.exit()


test_int_list = [1, 2, 3, 4, 4, 5, 6, 7, 9, 9]
test_string_list = ['one', 'two', 'three', 'four', 'five']

test_string_int_dict = {'First':1, 'Second':2, 'Third':3, 'Fifth':5}
test_int_int_dict = {1:5, 7:3, 8:2, 3:3}
test_string_double_dict = {'Scott':5.6, 'Jenny':9.3, 'Other Namer':4.7}
test_string_to_bool_dict = {'Tom':True, 'Jimmy':False, 'Kyle':True, 'Sarah':True}

def error_msg():
    print('This test crashed at runtime ...')
    traceback.print_exc(file=sys.stdout)

def run_Q1():
    if len(test_int_list) == student_file.Q1(test_int_list):
        return 1
    else: 
        return 0    

def run_Q2():
    temp_list = list(test_string_list) # used to deep copy, not just point to same list
    temp_list.append('movie')

    student_file.Q2(test_string_list)
    if temp_list == test_string_list:
        return 1
    return 0

def run_Q3():
    if 6 == student_file.Q3(test_int_list, 6):
        return 1
    return 0

def run_Q4():
    if student_file.Q4(test_int_list, 7) and not student_file.Q4(test_int_list, 19):
        return 1
    return 0

def run_Q5():
    joined_list = ''.join(test_string_list)
    returned_string = student_file.Q5(test_string_list)

    if joined_list == returned_string:
        return 1
    return 0

def run_Q6():
    solution_list = [1,2,3,4,5,6,7,8,9,10]

    if solution_list == student_file.Q6():
       return 1
    return 0

def run_Q7():
    solution_list = ['memory', 'is', 'the', 'key']
    returned_list = student_file.Q7()

    if solution_list == returned_list:
        return 1
    return 0

def run_Q8():
    empty_dict = {}
    solution_dict = {'Awesome Stuff':99}
    
    student_file.Q8(empty_dict, 'Awesome Stuff', 99)

    if solution_dict == empty_dict:
        return 1
    return 0

def run_Q9():
    if student_file.Q9(test_string_to_bool_dict, 'Sarah') and not \
        student_file.Q9(test_string_to_bool_dict, 'Jimmy'):
        return 1
    return 0

def run_Q10():
    if student_file.Q10(test_string_int_dict, 1) and not \
        student_file.Q10(test_string_int_dict, 7):
        return 1
    return 0

def run_Q11():
    if len(test_string_int_dict) == student_file.Q11(test_string_int_dict):
        return 1
    return 0

def run_Q12():    
    solution_list = [1, 2, 3, 5]
    returned_list = student_file.Q12(test_string_int_dict)

    if solution_list == returned_list:
        return 1
    return 0

def run_Q13():
    solution_list = ['First', 'Second', 'Third', 'Fifth'].sort()
    returned_list = student_file.Q12(test_string_int_dict).sort()

    if solution_list == returned_list:
        return 1
    return 0

def run_Q14():
    if student_file.Q14(test_int_int_dict, 1) and not student_file.Q14(test_int_int_dict, 5):
        return 1
    return 0
def run_Q15():

    if 2 == student_file.Q15(test_int_int_dict, 3):
        return 1
    return 0

