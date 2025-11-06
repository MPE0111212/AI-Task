def a_to_b(a, b):
    if a < b:
        print(a)
        a_to_b(a + 1, b)
    elif a > b:
        print(a)
        a_to_b(a - 1, b)
    else:
        print(a)


A, B = int(input("A: ")), int(input("B: "))
a_to_b(A, B)
