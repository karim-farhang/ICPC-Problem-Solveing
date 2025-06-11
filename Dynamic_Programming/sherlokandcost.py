def cost(B):
    As = [[1, B[j]] for j in range(len(B))]
    print(As)
    score = [0, 0]
    for i in range(1, len(B)):
        new_score = [0, 0]
        for p in [0, 1]:
            for q in [0, 1]:
                new_score[q] = max(new_score[q], score[p] + abs(As[i - 1][p] - As[i][q]))
        score[0] = new_score[0]
        score[1] = new_score[1]
    print(new_score)
    return max(score)
arr = [1,2,3]
print(cost(arr))