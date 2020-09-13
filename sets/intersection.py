if __name__ == '__main__':

    e_n = int(input())
    e = map(int, input().split(" "))
    f_n = int(input())
    f = map(int, input().split(" "))

    print(len(set(e).intersection(f)))