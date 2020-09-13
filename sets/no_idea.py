if __name__ == '__main__':
    n, m = input().split(" ")
    arr = input().split(" ")
    set_a, set_b = set(input().split(" ")), set(input().split(" "))
    happiness = 0

    for i in set_a:
        if i in set_a:
            happiness = happiness + 1
        elif i in set_b:
            happiness = happiness - 1
    print(happiness)
