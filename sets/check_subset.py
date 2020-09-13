if __name__ == '__main__':
    for x in range(int(input())):
        n_a, a, n_b, b = int(input()), set(input().split()), int(input()), set(input().split())
        print(True if a.issubset(b) else False)
