def f(max_n, n=0, n_1=1):
    if n > max_n:
        return
    print(n)
    return f(max_n, n + n_1, n)


f(max_n=int(input()))
