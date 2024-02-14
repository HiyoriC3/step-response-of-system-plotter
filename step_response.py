import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

sys_num = []
sys_den = []
num_menu = True
den_menu = True
num_ele_menu = True
den_ele_menu = True

def element_int():
    try:
        ele = float(input("Enter element : "))
    except ValueError:
        print("Invalid input Please enter number\n")
    else:
        return ele

while num_menu == True:
    try:
        sys_num_count = int(input("Enter number of numerator : "))
    except ValueError:
        print("Invalid input Please enter an integer\n")
    else:
        while num_ele_menu == True:
            for i in range(0, sys_num_count):
                num_ele = element_int()
                sys_num.append(num_ele)
            if None not in sys_num:
                num_ele_menu = False
                print("num = ",sys_num,"\n")
            else:
                sys_num = []
                print("Re-enter all elements again\n")
        num_menu = False

while den_menu == True:
    try:
        sys_den_count = int(input("Enter number of denominator : "))
    except ValueError:
        print("Invalid input Please enter an integer\n")
    else:
        while den_ele_menu == True:
            for i in range(0, sys_den_count):
                den_ele = element_int()
                sys_den.append(den_ele)
            if None not in sys_den:
                den_ele_menu = False
                print("den = ",sys_den,"\n")
            else:
                sys_num = []
                print("Re-enter all elements again\n")
        den_menu = False

TS=ctrl.tf(sys_num, sys_den)
t,y=ctrl.step_response(TS)
plt.plot(t,y)
plt.xlabel('Time (seconds)')
plt.ylabel('Output, y')
plt.title("Step Response")
plt.show()