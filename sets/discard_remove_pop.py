if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split(" ")))
    n_c = int(input())

    for i in range(n_c):
        inp = input().split(" ")
        if inp[0] == "pop":
            s.pop()
        elif inp[0] == "discard":
            s.discard(int(inp[1]))
        else:
            s.remove(int(inp[1]))
    print(sum(s))