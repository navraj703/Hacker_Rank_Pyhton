myList = []
if __name__ == '__main__':
    N = int(input())
    for i in range(0, N):
        temp_str = input()
        temp_arr = temp_str.strip().split(" ")
        cmd = temp_arr[0]
        # inserting:
        if cmd == 'insert':
            myList.insert(int(temp_arr[1]), int(temp_arr[2]))
        # print
        elif cmd == 'print':
            print(myList)
        # append
        elif cmd == 'append':
            myList.append(int(temp_arr[1]))
        # sort
        elif cmd == 'sort':
            myList.sort()
        # pop
        elif cmd == 'pop':
            myList.pop()
        # reverse
        elif cmd == 'reverse':
            myList.reverse()
        # remove
        elif cmd == 'remove':
            if len(myList) == 0:
                print("List is empty")
                continue
            val = int(temp_arr[1])
            myList.remove(val)