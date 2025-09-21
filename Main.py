import math
import matplotlib
from random import randint
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

def operation_finder(symbvols):
    op_f = []
    try:op_f.append(symbvols.index("+"))
    except:pass
    try:
        if symbvols.index("-") != 0:
            op_f.append(symbvols.index("-"))
    except:pass
    try:op_f.append(symbvols.index("*"))
    except:pass
    try:op_f.append(symbvols.index("**"))
    except:pass
    try:op_f.append(symbvols.index("/"))
    except:pass
    op_f2 = sorted(op_f)
    print("Operations first order",op_f2)
    return op_f2
def operation_uniter(operation):
    operation = str(operation)
    symbvols = []
    answer = 0
    print(operation[0])
    print("LEN: OPERATION",len(operation))
    for i in operation:
        symbvols.append(i)
    true_operation = []
    op_f = []
    ab = 0
    while ab<10:
        op_f = operation_finder(symbvols)
        if not(len(op_f) == 0 or 0 in op_f):
            a = symbvols[:op_f[0]]
            a = "".join(a)
            true_operation.append(a)
            true_operation.append(symbvols[op_f[0]])
            symbvols = symbvols[op_f[0]+1:]
        else:
            a = symbvols
            a = "".join(a)
            true_operation.append(a)
            break
        print(true_operation)
        print("------------------")
        print(symbvols)
        ab += 1
    print('===================')
    print("Выражение",true_operation)
    print('===================')
    return true_operation
def calc_answer(operation):
    while True:
        operation_list = ["**","*","/","+","-"]
        if "**" in operation:
            a = operation.index("**")
            b = float(operation[a-1])**float(operation[a+1])
        elif "*" in operation:
            a = operation.index("*")
            b = float(operation[a-1])*float(operation[a+1])
        elif "/" in operation:
            a = operation.index("/")
            b = float(operation[a-1])/float(operation[a+1])
        elif "+" in operation:
            a = operation.index("+")
            b = float(operation[a-1])+float(operation[a+1])
        elif "-" in operation:
            a = operation.index("-")
            b = float(operation[a-1])-float(operation[a+1])
        else:print("OPERATION FINISHED");break
        q = []
        q.append(b)
        operation = operation[:a-1]+q+operation[a+1+1:]
        print(operation)
while True:
    operation = get_needed()
    true_operation = operation_uniter(operation)
    calc_answer(true_operation)
    
    