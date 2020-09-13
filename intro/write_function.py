# Writing Functions ---->
if __name__ == '__main__':
    def is_leap(year):
        # Write your logic here
        if year % 4 == 0 and year % 100 != 0:
            leap = True
        elif year % 400 == 0:
            leap = True
        else:
            leap = False
        return leap


    print(is_leap(2019))
