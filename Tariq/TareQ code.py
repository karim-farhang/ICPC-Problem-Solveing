def count(coins, n, sum):
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    if n <= 0:
        return 0
    return count(coins, n - 1, sum) + count(coins, n, sum - coins[n - 1])


k, n = map(int, input().split(' '))
coins = [int(i) for i in input().split(' ')]
print(count(coins, n, k))
