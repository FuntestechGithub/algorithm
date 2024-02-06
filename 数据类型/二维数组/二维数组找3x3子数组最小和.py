'''
1  2  3
4  5  6
7  8  9

1  3  6
5  12 21
12 27 45


12 16
24 28
'''
def find_min_sum_subarray(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows < 3 or cols < 3:
        raise ValueError("The matrix should be at least 3x3 in size.")

    min_sum = float('inf')  # Initialize with positive infinity

    for i in range(rows - 2):  # Rows of the 3x3 subarray
        for j in range(cols - 2):  # Columns of the 3x3 subarray
            current_sum = sum(
                matrix[i][j:j + 3] +
                matrix[i + 1][j:j + 3] +
                matrix[i + 2][j:j + 3]
            )
            if current_sum < min_sum:
                min_sum = current_sum
                min_subarray = [
                    matrix[i][j:j + 3],
                    matrix[i + 1][j:j + 3],
                    matrix[i + 2][j:j + 3]
                ]

    return min_subarray, min_sum

def find_min_sum_subarray(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows < 3 or cols < 3:
        return None

    # Create a DP array to store the cumulative sum
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Calculate cumulative sum
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            dp[i][j] = matrix[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

    min_sum = float('inf')
    min_subarray = None

    for i in range(3, rows + 1):  # Rows of the 3x3 subarray
        for j in range(3, cols + 1):  # Columns of the 3x3 subarray
            current_sum = dp[i][j] - dp[i - 3][j] - dp[i][j - 3] + dp[i - 3][j - 3]

            if current_sum < min_sum:
                min_sum = current_sum

    
    return min_sum


def find_min_sum_subarray_dfs(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows < 3 or cols < 3:
        raise None

    min_sum = float('inf')


    def dfs(i, j, current_sum, path):
        nonlocal min_sum

        if i >= 3 and j >= 3:
            if current_sum < min_sum:
                min_sum = current_sum
            return

        if i < rows:
            dfs(i + 1, j, current_sum + sum(matrix[i]), path + [matrix[i]])

        if j < cols:
            dfs(i, j + 1, current_sum, path)

    dfs(0, 0, 0, [])

    return min_sum


# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

output = [
    [0, 0, 0, 0, 0],
    [0, 1, 3, 6, 10],
    [0, 6, 14, 24, 36],
    [0, 15, 33, 54, 78],
    [0, 28, 60, 96, 136]
]

min_sum = find_min_sum_subarray_dfs(matrix)
print("Minimum sum:", min_sum)



