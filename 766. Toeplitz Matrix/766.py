'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
Example 2:

Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].
'''


def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    for x in range(len(matrix[0])):
        y = 0
        while y < len(matrix[0]):
            try:
                if matrix[y][x] != matrix[y + 1][x + 1]:
                    return False
            except IndexError:
                pass
            y += 1
    for y in range(len(matrix)):
        x = 0
        while x < len(matrix[0]):
            try:
                if matrix[y][x] != matrix[y + 1][x + 1]:
                    return False
            except IndexError:
                pass
            x += 1
    return True
