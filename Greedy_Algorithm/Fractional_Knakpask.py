"""
50
60,100,120
10,20,30
"""
W = int(input())
v = [int(x) for x in input().split(',')]
w = [int(x) for x in input().split(',')]
items = [(v[i], w[i], float(v[i] / w[i])) for i in range(len(v))]
items.sort(key=lambda x: x[2], reverse=True)
profit = 0
for i in items:
    print(*i)
    if i[1] < W:
        W -= i[1]
        profit += i[0]
    else:
        profit += (W / i[1]) * i[0]
        W = 0
        break
        # capacity = int(capacity - (curWt * fraction))
print(profit)


class Solution:

    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, Items, n):

        # taking variable for current weight in knapsack.
        curr_weight = 0
        curr_value = 0

        # sorting items on basis of value/weight ratio.
        Items = sorted(Items, key=lambda x: (x.value / x.weight), reverse=True)

        # iterating over all the items.
        for i in range(n):

            # if currweight + itemâ€™s weight is less than or equal to W,
            # then we add the item's value to final value.
            if curr_weight + Items[i].weight <= W:
                curr_weight += Items[i].weight
                curr_value += Items[i].value

            # else we take the fraction of the that item's value
            # based on the remaining weight in knapsack.
            else:
                accomodate = W - curr_weight
                value_added = Items[i].value * (accomodate / Items[i].weight)
                curr_value += value_added
                break

                # returning final value.
        return curr_value