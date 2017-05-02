import time
print("we're defining exponent here")
def exponent_iterative(num1, num2):
    print("we're in the exponent function")
    total = num1
    for i in range(1,num2):
        total *= num1
        # same as total = total * num1
        print("The total at iteration ", i, "is", total)
    return total

#solution with pintouts
def exponent_recursive(num1, num2):
    print("I'm at level: ", num2)
    time.sleep(1)
    if num2 == 0:
        return 1
    final = (num1 * exponent_recursive(num1, num2-1))
    print(final)
    time.sleep(1)
    return final

#actual solution
def expo(num1, num2):
    if num2 == 0:
        return 1
    return num1*expo(num1, num2-1)


'''
print("definition done")
num1 = 2
num2 = 10
exponent(num1, num2)
print("all done!")
'''
print(exponent_recursive(2,6))
    
