import matplotlib
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from math import *

def get_needed():
    operation = input()
    #if ("-" not in operation) and  ("+" not in operation) and ("/" not in operation) and ("*" not in operation) and ("**" not in operation):
    #    print("MISTAKE NO OPERATOR")
    #    return 0
    if True:
        print("---------------")
        print(operation)
        print("---------------")
        return operation
def add_np(operation):
    operation1 = []
    operation2 = []
    need_np_list = ["s","c","t","a"]
    for i in range(len(operation)):operation1.append(operation[i])
    print("operation 1",operation1)
    for q in range (len(operation1)):
        operation2.append(operation1[q])
        try:
            if operation1[q+1] in need_np_list:
                operation2.append("np.")
        except:pass
    print("operation 2",operation2)
    operation = "".join(operation2)
    print("NP",operation)
    return operation
def transformtofx(operation,x_range=(-10, 10), num_points=1000):
    # Generate x values
    operation = add_np(operation)
    x = np.linspace(x_range[0], x_range[1], num_points)
    x_side = operation[operation.find("=")+1:]
    y_side = operation[:operation.find("=")]
    # Safe evaluation environment using locals
    try:
        # Define a safe local environment for eval
        allowed_locals = {'np': np, 'x': x}
        # Evaluate the function
        y = eval(x_side, {"__builtins__": None}, allowed_locals)
    except SyntaxError:
        print("Error: Invalid syntax in the function. Please check your input.")
        return

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'y = {operation}')
    plt.title('Plot of the Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()
#def build_grapf(operation):
#    color = Main.generate_color()
#    x = np.linspace(-10, 10, 1000)
#    y = x
#    y0 = x*0
#    fig = plt.figure(figsize = (10, 5))
#    plt.plot(x, y)
#    plt.axhline(y=0,label="ox axis", color='red', linestyle='--')
#    plt.axvline(x=0,label="oy axis", color='blue', linestyle=':')
#    plt.legend()
#    plt.grid(True, linestyle =':')
#    plt.title('TEST')
#    plt.xlabel('x-axis')
#    plt.ylabel('y-axis')
#    plt.show()
operation = get_needed()
transformtofx(operation)
#build_grapf(operation)