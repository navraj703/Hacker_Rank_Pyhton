if __name__ == '__main__':

    def split(word):
        return list(word)


    def mutate_string(string, position, character):
        temp_list = split(string)
        temp_list[position] = character
        temp_str = ''.join(temp_list)
        return temp_str
    # def mutate_string(string, position, character):
    #     return string[:position] + character + string[position + 1:]
