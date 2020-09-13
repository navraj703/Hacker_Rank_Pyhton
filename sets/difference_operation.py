# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n_a = input("")
    a = set(input().split(" "))
    n_b = input("")
    b = set(input().split(" "))
    res = len(a.difference(b))
    print(res)