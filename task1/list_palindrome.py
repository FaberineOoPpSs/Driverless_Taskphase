'''def check_palindrom(l):
    i = len(l) - 1
    l1 = list(l)
    t = []
    while i >= 0:
        t.append(l1[i])
        l1.pop()
        i = i - 1
    if t == l:
        return True
    return False'''
def check_palindrome(l):
    t = list(l)
    print(t)
    j = []
    #print(j)
    n = len(l) - 1
    def recur(t,n):
        if n < 0:
            return j
        else:
            temp = t[n]
            j.append(temp)
            #print(j)
            t.pop()
            recur(t, n - 1)
        return j
    palin = recur(t, n)
    return palin

def unique_list(l):
    
    for i in l:
        if l.count(i) > 1:
            t = l.index(i)
        
            for k in range(t + 1, len(l) - 1):
                if l[k] == i:
                    l.pop(k)
                    k = k - 1 
        if l.count(i) > 1:
            l.pop()
    
    return l

def char_hex_conv(cha):
    return format(ord(cha), "x")

def pyramid(l):
    space = len(l)
    t = 0
    lr = -1
    for i in range(len(l)):
        for s in range(space):
            print(' ', end = '')
        for j in range(t + 1):
            print(l[j],  sep = '', end = '')
        j = lr
        while j >= 0 and i > 0:
            print(l[j], sep = '', end = '')
            j = j - 1
        space = space - 1
        t = t + 1
        lr = lr + 1
        print('\n')
    
    sp = 2
    t = len(l) - 1
    k = len(l) - 2
    for i in range(len(l) - 1, 0, -1):
        for s in range(sp):
            print(' ', end = '')
        for j in range(t):
            print(l[j], sep = '', end = '')
        for j in range(k - 1, -1, -1):
            print(l[j], sep = '', end = '')
        sp = sp + 1
        t = t - 1
        k = k - 1
        print('\n')        

l_str = input("Enter only strings: ")
l = list(l_str)
print(l)
l_palin = check_palindrome(l)
if l_palin == l:
    print("List is palindrome!")
    print("There hexadecimal values are: ")
    u_l = unique_list(l)
    for i in u_l:
        print(i, " = ",char_hex_conv(i))
else:
    print("Not palindrome")
    pyramid(l)
    

