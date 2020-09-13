if __name__ == '__main__':
    num_of_countries = int(input())
    temp_list = []
    for i in range(num_of_countries):
        inp = input()
        temp_list.append(inp)
    print(len(set(temp_list)))
