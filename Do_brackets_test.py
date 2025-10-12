operation = input()
def turn_into_sqrbr(operation):
    try:
        for i in range(len(operation)):
            if operation[i] == "(":
                bracket_opening = i
            if operation[i] == ")":
                bracket_closing = i
                break
def do_bracket(operation):
    while True:
        brackets_open = operation.count("(")
        brackets_close = operation.count(")")
        print(brackets_open,brackets_close)
        if brackets_open != brackets_close:print("() are not equal - ERROR");return False
        elif brackets_open == 0 and brackets_close==0:print("NO () found");operation = eval(operation);return operation
        else:
            for i in range(len(operation)):
                if operation[i] == "(":
                    bracket_opening = i
                if operation[i] == ")":
                    bracket_closing = i
                    break
            print(bracket_closing)
            bracket_op = operation[bracket_opening+1:bracket_closing]
            print(bracket_op)
            bracket_op = eval(bracket_op)
            operation = operation[:bracket_opening]+str(bracket_op)+operation[bracket_closing+1:]
            print(operation)
        print(operation)
print(do_bracket(operation))