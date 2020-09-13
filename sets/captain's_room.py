if __name__ == '__main__':
    n, a = input(), input().split()
    set_1, set_2 = set(), set()
    for i in a:
        if i in set_1:
            set_2.add(i)
        else:
            set_1.add(i)
    print(list(set_1.difference(set_2))[0])
