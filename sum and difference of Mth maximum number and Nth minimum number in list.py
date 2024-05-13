def find_max_min_sum_diff(nums, M, N):
    nums.sort()
    max_num = nums[-M]
    min_num = nums[N - 1]
    print(f"{M}th Maximum Number = {max_num}")
    print(f"{N}th Minimum Number = {min_num}")
    print(f"Sum = {max_num + min_num}")
    print(f"Difference = {abs(max_num - min_num)}")
test_cases = [
    ([16, 16, 16, 16, 16], 0, 1),
    ([0, 0, 0, 0], 1, 2),
    ([-12, -78, -35, -42, -85], 3, 3),
    ([15, 19, 34, 56, 12], 6, 3),
    ([85, 45, 65, 75, 95], 5, 7)
]
for nums, M, N in test_cases:
    print("Test Case:")
    print("List of elements:", nums)
    print("M =", M)
    print("N =", N)
    find_max_min_sum_diff(nums, M, N)
    print()
