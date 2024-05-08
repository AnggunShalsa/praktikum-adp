def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def print_matrix(matrix, label):
    print(label)
    for row in matrix:
        print(row)

n = int(input("Masukkan ukuran matriks: "))
matrix_A = [[int(input(f"Masukkan elemen matriks A[{i}][{j}]: ")) for j in range(n)] for i in range(n)]
matrix_B = [[int(input(f"Masukkan elemen matriks B[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

print_matrix(matrix_A, "Matriks A:")
print_matrix(matrix_B, "Matriks B:")

matrix_C = matrix_multiplication(matrix_A, matrix_B)
print_matrix(matrix_C, "Matriks C (Hasil perkalian matriks A dan B):")

matrix_A_transpose = transpose(matrix_A)
matrix_B_transpose = transpose(matrix_B)

matrix_D = matrix_addition(matrix_A_transpose, matrix_B_transpose)
print_matrix(matrix_D, "Matriks D (Hasil penjumlahan matriks A transpose dan B transpose):")