def fib(values):
    term=1
    lo=[1]
    for n in range(0,values-1):
        lo.append(term)
        term=lo[len(lo)-1]+lo[len(lo)-2]
    print(lo)
