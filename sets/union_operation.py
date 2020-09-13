if __name__ == '__main__':
    n_a = input("")
    a = set(input().split(" "))
    n_b = input("")
    b = set(input().split(" "))
    print(len(a) + len(b) - len(a.intersection(b)))
