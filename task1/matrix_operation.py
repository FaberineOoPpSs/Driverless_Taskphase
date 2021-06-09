import math
'''Several comment statements have been added to fix understand errors in this module, do uncomment them to check and verify the concept building in several loops'''
class Operations():
    def __init__(self, matrix):
        self.mat = matrix
    def calc_det(self):
        def recur(m):
            n = len(m)
            sum = 0
            a = list(m)
            temp = [0] * (n - 1)
            for i in range(n - 1):
                temp[i] = [0] * (n - 1)
            if n == 0:
                return a
            if n == 1:
                return a
            if n == 2:
                return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
            if n > 2:
                for i in range(n):
                    for j in range(n - 1):
                        for p in range(n - 1):
                            if i == 0:
                                temp[j][p] = a[j + 1][p + 1]
                            if i > 0 and i < n - 1:
                                if p < i:
                                    temp[j][p] = a[j + 1][p]
                                if p > i:
                                    temp[j][p] = a[j + 1][p + 1]
                            if i == n - 1:
                                temp[j][p] = a[j + 1][p]
                        #print(temp)

                    sum = sum + int(math.pow(-1,i)) * a[0][i] * recur(temp)
                    #print(-1**i)    
                    #print(sum)
                return sum
        m = self.mat
        mat = recur(m)
        return mat
    
    def calc_adj(self):
        m = self.mat
        n = len(m)
        a = list(m)
        
        adj_final = list(m)
        if n < 2:
            str = "Pls enter a matrix of order n > = 2"
            return str
        if n == 2:
            adj_final[0][0] = a[1][1]
            adj_final[1][1] = a[0][0]
            adj_final[0][1] = - a[0][1]
            adj_final[1][0] = - a[1][0]
            return adj_final
        if n > 2:
            def trans_conv(row, col, m):
                trans_mat = [0] * col
                for k in range(col):
                    trans_mat[k] = [0] * row
                for i in range(row):
                    for j in range(col):
                        trans_mat[j][i] =  m[i][j]
                return trans_mat
            b = [0] * n
            for i in range(n):
                b[i] = [0] * n
            temp = [0] * (n - 1)
            for i in range(n - 1):
                temp[i] = [0] * (n - 1)
            for i in range(n):
                for j in range(n):
                    for k in range(n - 1):
                        for p in range(n - 1):
                            if i == 0:
                                if j == 0:
                                    temp[k][p] = a[k + 1][p + 1]
                                if j > 0 and j < n - 1:
                                    if p < j:
                                        temp[k][p] = a[k + 1][p]
                                    if p > j:
                                        temp[k][p] = a[k + 1][p + 1]
                                if j == n - 1:
                                    temp[k][p] = a[k + 1][p]
                            if i > 0 and i < n - 1:
                                if j == 0:
                                    if k < i:
                                        temp[k][p] = a[k][p + 1]
                                    if k == i:
                                        temp[k][p] = a[k + 1][p + 1]
                                    if k > i:
                                        temp[k][p] = a[k + 1][p + 1]
                                if j > 0 and j < n - 1:
                                    if k < i:
                                        if p < j:
                                            temp[k][p] = a[k][p]
                                        if p == j:
                                            temp[k][p] = a[k][p + 1]
                                        if p > j:
                                            temp[k][p] = a[k][p + 1]
                                    if k == i:
                                        if p < j:
                                            temp[k][p] = a[k + 1][p]
                                        if p == j:
                                            temp[k][p] = a[k + 1][p + 1]
                                        if p > j:
                                            temp[k][p] = a[k + 1][p + 1]
                                    if k > i:
                                        if p < j:
                                            temp[k][p] = a[k + 1][p]
                                        if p == j:
                                            temp[k][p] = a[k + 1][p + 1]
                                        if p > j:
                                            temp[k][p] = a[k + 1][p + 1]
                                if j == n - 1:
                                    if k < i:
                                        temp[k][p] = a[k][p]
                                    if k == i:
                                        temp[k][p] = a[k + 1][p]
                                    if k > i:
                                        temp[k][p] = a[k + 1][p]
                            if i == n - 1:
                                if  j == 0:
                                    temp[k][p] = a[k][p + 1]
                                if j > 0 and j < n - 1:
                                    if p < j:
                                        temp[k][p] = a[k][p]
                                    if p > j:
                                        temp[k][p] = a[k][p + 1]
                                if j == n - 1:
                                    temp[k][p] = a[k][p]
                                    #print("temp last ",temp)
                    #print('Temp: ',temp)
                    c = Operations(temp)
                    b[i][j] = int(math.pow(-1, (i + j))) * c.calc_det()
            #print('adjoint not-converted: ',b)
            adj_final = trans_conv(n, n, b)
            return adj_final
    def calc_inv(self):
        m = self.mat
        n = len(m)
        op = Operations(m)
        det = op.calc_det()
        adj = op.calc_adj()
        if det == 0:
            str = "Inverse dosen't exist"
            return str
        else:
            inv = [0] * (n)
            for i in range(n):
                inv[i] = [0] * (n)
            for i in range(n):
                for j in range(n):
                    inv[i][j] = adj[i][j] / det                      
            return inv
