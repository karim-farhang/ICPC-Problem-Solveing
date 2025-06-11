# --- Kadane's Algorithm ---
# Given an array Arr[] of N integers.
# Find the contiguous sub-array(containing at least one number)
# which has the maximum sum and return its sum.
def maxSubArraySum(a, size):
    max_so_far = -9999999 - 1
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
Arr = [1, 2, 3, -2, 5]
print(maxSubArraySum(Arr, len(Arr)))
