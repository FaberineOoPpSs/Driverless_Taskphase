def unique_tup(tup):
    
    l = list(tup)
    for i in l:
        if l.count(i) > 1:
            t = l.index(i)
        
            for k in range(t + 1, len(l) - 1):
                if l[k] == i:
                    l.pop(k)
                    k = k - 1 
        if l.count(i) > 1:
            l.pop()
    
    tup_final = tuple(l)
    return tup_final

def sum_tup(tup,n):
    sum = 0
    if n >= 1:
        k = tup[n]
        sum = sum + k + sum_tup(tup,n-1)
    if n == 0:
        return sum + tup[0]
    return sum

t = tuple(eval(input("Enter the values to be stored in tuple: ")))
tup_final = unique_tup(t)
tup_sum = sum_tup(tup_final, len(tup_final) -1 )
print("Final tuple: ", tup_final)
print("Sum of tuple: ", tup_sum)
