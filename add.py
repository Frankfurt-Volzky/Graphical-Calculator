def add_np():
    operation = input()
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
add_np()