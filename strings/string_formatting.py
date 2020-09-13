if __name__ == '__main__':
    def print_formatted(n):
        w = len(str(bin(n))[2:])
        for i in range(1, n + 1, 1):
            o = str(oct(i))[2:]
            h = str(hex(i))[2:]
            h = h.upper()
            b = str(bin(i))[2:]
            d = str(i)
            print('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(d, o, h, b, width=w))
