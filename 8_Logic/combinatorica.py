# факториал
def fact(n):
    answer = 1
    for i in range(2, n + 1):
        answer *= i
    return answer


# сочетание из n по m
def Cnm(n, m):
    return fact(n) / (fact(n - m) * fact(m))


# сочетание с повторением из n по m
def Cnm_p(n,m):
    return fact(n+m-1) / (fact(n-1) * fact(m))


# размещение из n по m
def Rnm(n, m):
    return Cnm(n, m) * fact(m)


# размещение с повторением из n по m
def Rnm_p(n, m):
    return n**m


# перестановка с повторение из n по m
def Per_p(n, m):
    a = 1
    for i in m:
        a *= fact(i)
    return fact(n) / a






