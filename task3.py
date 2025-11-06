def check_exp_of_two(n):
    print(n)
    if n < 2:
        print("NO")
    elif n == 2:
        print("YES")
    else:
        check_exp_of_two(n * 0.5)


check_exp_of_two(int(input()))
