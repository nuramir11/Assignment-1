def inputMatrix(rows, cols):
    matrix = []
    print(f"Enter the elements for a matrix of size {rows}x{cols}:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def multiplyMatrices(A, B):
    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])
    if colsA != rowsB:
        return None
    result = [[0] * colsB for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += A[i][k] * B[k][j]
    return result

def displayMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    rowsA = int(input("Enter the number of rows of the first matrix: "))
    colsA = int(input("Enter the number of columns of the first matrix:"))
    A = inputMatrix(rowsA, colsA)
    rowsB = int(input("Enter the number of rows of the second matrix: "))
    colsB = int(input("Enter the number of columns of the second matrix: "))
    B = inputMatrix(rowsB, colsB)
    result = multiplyMatrices(A, B)
    if result:
        print("The result of matrix multiplication:")
        displayMatrix(result)
    else:
        print("Multiplication is impossible because the number of columns of the first matrix is not equal to the number of rows of the second matrix.")

if __name__ == "__main__":
    main()
