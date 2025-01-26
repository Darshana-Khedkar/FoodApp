def longestArithmeticSubsequence(arr):
    if not arr:
        return 0
    n = len(arr)
    dp = [{} for _ in range(n)]  # List of empty dictionaries
    max_length = 1

    for i in range(n):
        for j in range(i):
            diff = arr[i] - arr[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
            else:
                dp[i][diff] = 2
            max_length = max(max_length, dp[i][diff])
    return max_length


if __name__ == '__main__':
    arr_count = int(input("Enter the number of elements in the array: ").strip())

    print(f"Enter {arr_count} space-separated integers for the array:")

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    print(f"ARRAY IS: {arr}")

    result = longestArithmeticSubsequence(arr)
    print(f"The length of the longest arithmetic subsequence is: {result}")
