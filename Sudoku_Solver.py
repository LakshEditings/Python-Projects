# Sudoku Solver Using Simple BackTracing Algorithm
# By LakshEditings    linkedin.com/in/v-lakshen-b1103a213/
# 20 Minutes

# Enter The Sudoku (Nested List Format)
given = [
    [0, 2, 4, 3, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 0, 0, 7],
    [0, 5, 8, 0, 0, 2, 4, 0, 0],
    [4, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 1, 0, 0, 0, 6, 7, 0],
    [3, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 9, 2, 1, 0]
]

# Print Given Sudoku
def print_given(given):
    for i in range(9):
        for j in range(9):
            print(given[i][j], end=' ')
            if (j % 3 == 2):
                print('│', end=' ')
        print()
        if (i % 3 == 2):
            print('━' * 16)

# Find First Mty Cell
def find_first_mty(given):
    for i in range(9):
        for j in range(9):
            if (given[i][j] == 0):
                return (i,j)
    return None

# Check The Number Is Valid Or Not
def is_valid(given, num, row, col):
    # Check If  The Number Is In 3x3
    for i in range(9):
        if (given[row][i] == num or given[i][col] == num or given[3*(row//3)+i//3][3*(col//3)+i%3] == num):
            return False
    return True

# Main Function
def solve(given):
    mty = find_first_mty(given)
    if mty is None:
        return True

    row, col = mty
    for num in range(1, 10):
        if is_valid(given, num, row, col):
            given[row][col] = num
            if solve(given):
                return True
            given[row][col] = 0
    return False

# Print Result
print("Given:")
print_given(given)
if solve(given):
    print("Solved")
    print_given(given)
else:
    print("InValid!!")

    
