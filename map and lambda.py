def fibonacci(nterms):
    a = 0
    b = 1
    l = []

    if nterms == 0:
        pass
    elif nterms == 1:
        l.append(a)

    else:
        l.append(a)
        l.append(b)
        for i in range(2, nterms):
            c = a + b
            a = b
            b = c
            l.append(c)
        return l 


cube = lambda x: x**3


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
 