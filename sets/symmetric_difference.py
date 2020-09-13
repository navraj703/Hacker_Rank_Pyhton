if __name__ == '__main__':
    a_n = int(input("Number of Element in set A\n"))
    a = set(map(int, input().split(" ")))
    b_n = int(input("Number of Element in set B\n"))
    b = set(map(int, input().split(" ")))
    union_set = a.union(b)

    for val in a.intersection(b):
        union_set.remove(val)
    for i in sorted(union_set):
        print(i)
