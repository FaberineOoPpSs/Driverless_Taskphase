from matrix_operation import Operations
def mat_conv(row, col, m):
    mat = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(m[row * i + j ])
        mat.append(temp)
    return mat

def mat_mul(m1, m2, row1, col1, col2):
    final_mat = [0] * row1 
    for i in range(row1):
        final_mat[i] = [0] * col2 
    for m in range(row1):
        for n in range(col2):
            temp = 0
            for k in range(col1):
                temp = temp + m1[m][k] * m2[k][n]
            final_mat[m][n] = temp
    return final_mat

n = int(input("Enter the order of square matrices: "))
a = list(eval(input("Enter the value of matrix A: ")))
b = list(eval(input("Enter the value of matrix B: ")))

A = mat_conv(n, n, a)
B = mat_conv(n, n, b)
inva = Operations(B)
invb = Operations(A)
invA = inva.calc_inv()
invB = invb.calc_inv()
print("Inverse of matrix A: ", invA)
print("Inverse of matrix B: ", invB)
A_invB = mat_mul(A, invB, n, n, n)
invA_invB = mat_mul(invA, invB, n, n, n)

print(" ---A x (inverse(B))--- ")
print(A_invB)
print(" --- inverse(A) x inverse(B)--- ")
print(invA_invB)