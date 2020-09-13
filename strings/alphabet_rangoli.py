if __name__ == '__main__':
    start = 97
    end = 97


    def print_line(n, i):
        length = 4 * n - 3
        diff = int(length / 2)
        cp = 97 + n - 1
        for j in range(length):
            if (j % 2) != 0:
                print('-', end="")
            elif j <= diff + 2 * i and j >= diff - 2 * i:
                print(chr(cp), end="")
                if j < diff:
                    cp = cp - 1
                else:
                    cp = cp + 1
            else:
                print('-', end="")


    def print_rangoli(n):
        global end
        end = start + n - 1
        for i in range(n - 1):
            print_line(n, i)
            print('')
        i = n - 1
        while i >= 0:
            print_line(n, i)
            print('')
            i = i - 1
