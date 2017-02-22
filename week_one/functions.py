name = "troy"
other_name = "alex"

# public static String func_name() 

def Q1():
    print("Hello World!")

def Q2(param):
    print(param)

def reversal(param):
    rev_name = ""
    for char in param:
        rev_name = char + rev_name
    print(rev_name)

Q1()
Q2(other_name)

reversal("reverse this string")
