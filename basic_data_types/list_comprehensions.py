if __name__ == '__main__':
    x, y, z, n = int(input()), int(input()), int(input()), int(input()),
    output = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    output.append([i, j, k])
    print(output)
