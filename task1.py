def all_to_n(n):
    if not n:
        return
    print(n)
    all_to_n(n - 1)


all_to_n(int(input()))
