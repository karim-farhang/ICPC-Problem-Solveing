operator = "+-*/^"


def isOperator(c):
    return c in operator


def isOperand(c):
    return c >= 'A' and c <= 'Z'


def getPrce(c):
    res = 0
    for i in operator:
        res += 1
        if i == c:
            if i in '-/':
                res -= 1
            break
    return res


def getLowestPrec(subExp):
    low = 100
    pCount = 0
    for i in subExp:
        if pCount == 0 and isOperator(i):
            opPrec = getLowestPrec(i)

            if opPrec < low:
                low = opPrec
            elif i == '(':
                pCount += 1
            elif i == ')':
                pCount -= 1
    return low


def toInfix(experation):
    result = ''
    stack = ['', '', '', '', '', '', '', '', '', '', '', '']
    for c in experation:
        if isOperand(c):
            stack.append(c)
        else:
            ex2 = stack.pop()
            ex1 = stack.pop()

            pOper = getPrce(c)

            lpEx2 = getLowestPrec(ex2)
            lpEx1 = getLowestPrec(ex1)

            if lpEx2 < pOper:
                ex2 = '(' + ex2 + ')'
            if lpEx1 < pOper:
                ex1 = '(' + ex1 + ')'
            newExp = ex1 + c + ex2
            stack.append(newExp)
    result = stack.pop()


print(toInfix('ABC++'))
