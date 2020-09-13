if __name__ == '__main__':
    def swap_case(s):
        answer = ""
        for i in s:
            if i.islower():
                answer += i.upper()
            elif i.isupper():
                answer += i.lower()
            else:
                answer += i
        return answer