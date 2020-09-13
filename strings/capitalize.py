if __name__ == '__main__':
    def solve(s):
      temp_list  = s.split(" ")
      answer  = ""
      for i in temp_list:
        answer += i[:1].upper() + i[1:] + " "
      return answer