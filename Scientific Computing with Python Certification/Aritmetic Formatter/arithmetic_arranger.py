import re


def arithmetic_arranger(problems, arranged=False):
    if len(problems) < 1: return ''
    if len(problems) > 5: return "Error: Too many problems."

    # check *,\, ++, *+
    for problem in problems:
        matches = re.findall(r'(\s(\+|\-)\s(?!(\+|\-)))', problem)
        if len(matches) == 0: return "Error: Operator must be '+' or '-'."

    # check contain digits
    for problem in problems:
        matches = re.findall(r'[a-z]', problem)
        if len(matches) > 0: return "Error: Numbers must only contain digits."

    for problem in problems:
        matches = re.findall(r'((\b)\d{1,4})\s(\+|\-)\s(\d{1,4}(?!\d))',
                             problem)
        if len(matches) == 0:
            return "Error: Numbers cannot be more than four digits."

    # formatear el string
    operand1 = "{:2}".format("")
    operand2 = ""
    dashes = ""
    resOp = "{:1}".format("")
    for i, problem in enumerate(problems):
        matches = problem.split(" ")
        op1str = matches[0]
        op1 = int(op1str)
        op2str = matches[2]
        op2 = int(op2str)
        operation = matches[1]
        maxlenth = len(op1str) if len(op1str) >= len(op2str) else len(op2str)

        # assign operand 1
        operand1 += "{:>{op}}{:6}".format(op1, " ", op=maxlenth)
        # assign operand 2
        operand2 += "{op} {:>{lenth}}{:4}".format(op2, " ", lenth=maxlenth, op=operation)
        # assign dashes
        dashes += "{:-<{op}}{:4}".format("", " ", op=maxlenth + 2)
        # assign result
        if operation == '+':
            res = op1 + op2
        elif operation == '-':
            res = op1 - op2
        numSep = 4 if maxlenth == 3 else 3
        if arranged:
            resOp += "{:{lenth}}{:{sep}}".format(res, " ", sep=5, lenth=numSep)

    if arranged:
        arranged_problems = operand1.rstrip() + '\n' + operand2.rstrip() + '\n' + dashes.rstrip() + '\n' + resOp.rstrip()
    else:
        arranged_problems = operand1.rstrip() + '\n' + operand2.rstrip() + '\n' + dashes.rstrip()
    return arranged_problems
