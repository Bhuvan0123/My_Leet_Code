# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

# Return the smallest index i at which either a row or a column will be completely painted in mat.
def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        positions = {mat[r][c]: (r, c) for r in range(rows) for c in range(cols)}
        rcount = [cols] * rows
        ccount = [rows] * cols
        for index, value in enumerate(arr):
            row, col = positions[value]
            rcount[row] -= 1
            ccount[col] -= 1
            if rcount[row] == 0 or ccount[col] == 0:
                return index
        return -1