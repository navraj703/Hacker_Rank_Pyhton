if __name__ == '__main__':

    def wrap(string, max_width):
        s = ""
        for c in range(0,len(string),max_width):
            s += string[c:c+max_width] + "\n"
        return s