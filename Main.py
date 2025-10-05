import math
import matplotlib
from random import randint

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
def operation_finder(symbvols):
    op_f = []
    try:op_f.append(symbvols.index("+"))
    except:pass
    try:
        if symbvols.index("-") != 0:
            op_f.append(symbvols.index("-"))
    except:pass
    try:op_f.append(symbvols.index("^"))
    except:pass
    try:op_f.append(symbvols.index("*"))
    except:pass
    try:op_f.append(symbvols.index("/"))
    except:pass
    try:op_f.append(symbvols.index("%"))
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
def check_fordouble(true_operation):
    for i in range(len(true_operation)):
        if "*" in true_operation[i] and len(true_operation[i]) >1:
            true_operation[i] = true_operation[i][1:]
            true_operation[i-1] = "**"
        elif "/" in true_operation[i] and len(true_operation[i]) >1:
            true_operation[i] = true_operation[i][1:]
            true_operation[i-1] = "//"
    return true_operation  
def find_trigogeometry(operation):
    status = False
    for i in range(len(operation)):
        try:
            if "sin" in operation[i]:status=True
            elif "cos" in operation[i]:status=True
            elif "tg" in operation[i] or "tan" in operation[i]:status=True
            elif "сtg" in operation[i] or "сtan" in operation[i]:status=True
            elif "asin" in operation[i]:status=True
            elif "acos" in operation[i]:status=True
            elif "atan" in operation[i] or "atg" in operation[i]:status=True
            elif "atan2" in operation[i] or "atg2" in operation[i]:status=True
        except:pass
    return status
def calc_answer(operation):
    while True:
        operation_list = ["**","^","*","/","+","-"]
        status = find_trigogeometry(operation)
        print(operation,status)
        if status==True:
            for i in range(len(operation)):
                print(operation[i])
                try:
                    pre_op = operation
                    if "sin(" in operation[i] and operation[i][0] == "s":
                        print("FOUND SIN")
                        sina = operation[i]
                        #sina = sina[sina.find("("):sina.find[")"]]
                        aa = sina.find("(")+1
                        bb = sina.find(")")
                        sina = sina[aa:bb]
                        print(sina)
                        h = math.sin(int(sina) * math.pi / 180)
                        print("SIN:",h)
                        h = round(h,2)
                        operation[i] = str(h)
                    elif "cos(" in operation[i] and operation[i][0] == "c":
                        print("FOUND COS")
                        sina = operation[i]
                        #sina = sina[sina.find("("):sina.find[")"]]
                        aa = sina.find("(")+1
                        bb = sina.find(")")
                        sina = sina[aa:bb]
                        print(sina)
                        h = math.cos(int(sina) * math.pi / 180)
                        print("COS:",h)
                        h = round(h,2)
                        operation[i] = str(h)
                    elif "tg(" in operation[i] or "tan(" in operation[i] and operation[i][0] == "t":
                        print("FOUND TG")
                        sina = operation[i]
                        #sina = sina[sina.find("("):sina.find[")"]]
                        aa = sina.find("(")+1
                        bb = sina.find(")")
                        sina = sina[aa:bb]
                        print(sina)
                        h = math.tan(int(sina) * math.pi / 180)
                        print("TG:",h)
                        h = round(h,2)
                        operation[i] = str(h)
                    elif "сtg(" in operation[i] or "сtan(" in operation[i] and operation[i][0] == "c":
                        print("FOUND CTG")
                        sina = operation[i]
                        #sina = sina[sina.find("("):sina.find[")"]]
                        aa = sina.find("(")+1
                        bb = sina.find(")")
                        sina = sina[aa:bb]
                        print(sina)
                        h = 1/math.tan(int(sina) * math.pi / 180)
                        print("CTG:",h)
                        h = round(h,2)
                        operation[i] = str(h)
                    elif "asin(" in operation[i] and operation[i][0] == "a" and operation[i][1] == "s":
                        print("FOUND aSIN")
                        sina = operation[i]
                        #sina = sina[sina.find("("):sina.find[")"]]
                        aa = sina.find("(")+1
                        bb = sina.find(")")
                        sina = sina[aa:bb]
                        print(sina)
                        h = math.asin(sin(pi/int(sina)))
                        print("aSIN:",h)
                        h = round(h,2)
                        operation[i] = str(h)
                    elif "acos(" in operation[i] and operation[i][0] == "a" and operation[i][1] == "c":
                        print("FOUND aCOS")
                        sina = operation[i]
                        #sina = sina[sina.find("("):sina.find[")"]]
                        aa = sina.find("(")+1
                        bb = sina.find(")")
                        sina = sina[aa:bb]
                        print(sina)
                        h = math.acos(cos(pi/int(sina)))
                        print("aCOS:",h)
                        h = round(h,2)
                        operation[i] = str(h)
                    elif "atan(" in operation[i] or "atg(" in operation[i] and operation[i][0] == "a" and operation[i][1] == "t":
                        print("FOUND aTAN")
                        sina = operation[i]
                        #sina = sina[sina.find("("):sina.find[")"]]
                        aa = sina.find("(")+1
                        bb = sina.find(")")
                        sina = sina[aa:bb]
                        print(sina)
                        h = math.atan(tan(pi/int(sina)))
                        print("aTAN:",h)
                        h = round(h,2)
                        operation[i] = str(h)
                    elif "atan2(" in operation[i] or "atg2(" in operation[i]:
                        print("FOUND aTAN")
                        sina = operation[i]
                        #sina = sina[sina.find("("):sina.find[")"]]
                        aa = sina.find("(")+1
                        bb = sina.find(")")
                        sina = sina[aa:bb]
                        sina = sina.split(",")
                        print("SPLIT:",sina)
                        h = math.atan2(int(sina[0]),int(sina[1]))
                        print("aTAN2:",h)
                        h = round(h,2)
                        operation[i] = str(h)
                    print("OPERATION AFTER TRIOGONOMETRY:",operation)
                except:pass
        elif "**" in operation:
            a = operation.index("**")
            b = float(operation[a-1])**float(operation[a+1])
            print("EXECUTED **")
        elif "^" in operation:
            a = operation.index("^")
            b = float(operation[a-1])**float(operation[a+1])
            print("EXECUTED ^")
        elif "*" in operation:
            a = operation.index("*")
            b = float(operation[a-1])*float(operation[a+1])
            print("EXECUTED *")
        elif "/" in operation:
            a = operation.index("/")
            b = float(operation[a-1])/float(operation[a+1])
            print("EXECUTED /")
        elif "//" in operation:
            a = operation.index("//")
            b = float(operation[a-1])//float(operation[a+1])
            print("EXECUTED //")
        elif "%" in operation:
            a = operation.index("%")
            b = float(operation[a-1])%float(operation[a+1])
            print("EXECUTED %")
        elif "+" in operation:
            a = operation.index("+")
            b = float(operation[a-1])+float(operation[a+1])
            print("EXECUTED +")
        elif "-" in operation:
            a = operation.index("-")
            b = float(operation[a-1])-float(operation[a+1])
            print("EXECUTED -")
        else:print("OPERATION FINISHED");break
        try:
            q = []
            q.append(b)
            operation = operation[:a-1]+q+operation[a+1+1:]
            print(operation)
        except:pass
        if len(operation) <= 1:break
    answer = operation[0]
    try: answer = int(answer)
    except:pass
    return answer
while True:
    operation = get_needed()
    text = operation
    if "(" in operation:
        print("FOUND (), start alogirithm with them")
    true_operation = operation_uniter(operation)
    true_operation = check_fordouble(true_operation)
    answer = calc_answer(true_operation)
    print(text,"=",answer)
    