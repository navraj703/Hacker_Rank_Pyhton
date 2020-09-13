if __name__ == '__main__':
    n_a, a = int(input()), set(input().split())
    for i in range(int(input())):
        method, num_of_elem = input().split()
        my_set = set(input().split())
        if method == "intersection_update":
            a.intersection_update(my_set)
        elif method == "update":
            a.update(my_set)
        elif method == "symmetric_difference_update":
            a.symmetric_difference_update(my_set)
        else:
            a.difference_update(my_set)
    print(sum(set(map(int, a))))
