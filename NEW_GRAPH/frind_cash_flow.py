def getMin(arr, n):
    minInd = 0
    for i in range(1, n):
        if arr[i] < arr[minInd]:
            minInd = i
    return minInd


def getMax(arr, n):
    maxInd = 0
    for i in range(1, n):
        if arr[i] > arr[maxInd]:
            maxInd = i
    return maxInd


def minOf2(x, y):
    return x if x < y else y


def minCashFlowRec(amount, n):
    mxCredit = getMax(amount, n)
    mxDebit = getMin(amount, n)
    if amount[mxCredit] == 0 and amount[mxDebit] == 0:
        return 0
    min = minOf2(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= min
    amount[mxDebit] += min
    print("Person ", mxDebit, " pays ", min, " to ", "Person ", mxCredit)
    minCashFlowRec(amount, n)


def minCashFlow(graph, n):
    amount = [0 for i in range(n)]
    for p in range(n):
        for i in range(n):
            amount[p] += (graph[i][p] - graph[p][i])
    minCashFlowRec(amount, n)


graph = [[0, 1000, 2000],
         [0, 0, 5000],
         [0, 0, 0]]
n = 3
minCashFlow(graph, n)
