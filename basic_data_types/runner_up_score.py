from distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    set_temp = set(arr)
    final_ar = list(set_temp)
    final_ar.sort()
    print(final_ar[-2])