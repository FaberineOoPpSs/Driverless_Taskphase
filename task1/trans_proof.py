def mat_conv(row, col, l):
    i = 0
    mat = [0] * row
    for m in range(row):
        mat[m] = [0] * col
    for m in range(row):
        temp = []
        for n in range(col):
            mat[m][n] = l[i]
            i = i + 1
    return mat


def trans_conv(row, col, m):
    trans_mat = [0] * col
    for k in range(col):
        trans_mat[k] = [0] * row
    for i in range(row):
        for j in range(col):
            trans_mat[j][i] =  m[i][j]
    return trans_mat

def mat_product(row1, col1, col2, m1, m2):
    final_mat = [0] * row1 
    for i in range(row1):
        final_mat[i] = [0] * col2 
    for m in range(row1):
        for n in range(col2):
            temp = 0
            for k in range(col1):
                temp = temp + m1[m][k] * m2[k][n]
            final_mat[m][n] = temp
    return final_mat, row1, col2

row1 = int(input("Enter no. of rows for Matrix A: "))
col1 = int(input("Enter no. of colomns for Matrix A(this will also be row size of Matrix B): "))
A = list(eval(input("Enter values of Matrix A: ")))
col2 = int(input("Enter no. of colomns for Matrix B: "))
B = list(eval(input("Enter values for Matrix B: ")))

row2 = col1

A = mat_conv(row1, col1, A)
B = mat_conv(row2, col2, B)

A_trans = trans_conv(row1, col1, A)
row1_trans = col1
col1_trans = row1
B_trans = trans_conv(row2, col2, B)
row2_trans = col2
col2_trans = row2
#print("Transpose of matrix A:",A_trans)
#print("Transpose of matrix B:",B_trans)

AB, row, col = mat_product(row1, col1, col2, A, B)
AB_trans = trans_conv(row, col, AB)
#print('trans(AB): ',AB_trans)

Bt_At, row_product_trans, col_product_trans = mat_product(row2_trans, col2_trans,col1_trans, B_trans, A_trans)
#print("trans(A) x trans(B): ", At_Bt)

if AB_trans == Bt_At:
    print("transpose of (AB) is: ", AB_trans)
    print("Product of transpose(B) and transpose(A) is: ", Bt_At)
    print(" Since both of them are same hence correct")

else: 
    print("There is either problem in program or the data you have entered is not based on formula for transpose or product of matrices!")
    print(AB, AB_trans)
    print(Bt_At)
