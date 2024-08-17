class MyMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.mat = []

    def getter(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(int(input(f'Enter data for: MAT[{i}][{j}]: ')))
            self.mat.append(row)

    def __str__(self):
        result = ""
        for i in range(self.rows):
            for j in range(self.cols):
                result += f"{self.mat[i][j]}\t"
            result += "\n"
        return result

    def additionOfMatrices(self, mat: 'MyMatrix'):
        if self.rows == mat.rows and self.cols == mat.cols:
            result = MyMatrix(self.rows, self.cols)
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.mat[i][j] + mat.mat[i][j])
                result.mat.append(row)
            return result
        else:
            print("Matrices cannot be added due to different dimensions")
            return None

# Driver code
if __name__ == "__main__":
    # Create the first matrix
    print("Enter details for the first matrix:")
    rows1 = int(input("Enter the number of rows: "))
    cols1 = int(input("Enter the number of columns: "))
    matrix1 = MyMatrix(rows1, cols1)
    matrix1.getter()

    # Create the second matrix
    print("Enter details for the second matrix:")
    rows2 = int(input("Enter the number of rows: "))
    cols2 = int(input("Enter the number of columns: "))
    matrix2 = MyMatrix(rows2, cols2)
    matrix2.getter()

    # Display the matrices
    print("First Matrix:")
    print(matrix1)

    print("Second Matrix:")
    print(matrix2)

    # Add the matrices
    result_matrix = matrix1.additionOfMatrices(matrix2)
    if result_matrix:
        print("Resultant Matrix after Addition:")
        print(result_matrix)
