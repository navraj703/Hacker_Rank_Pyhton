if __name__ == '__main__':

    player_a = 0  # Vowel
    player_b = 0  # Constant
    sub_strings = []
    VOWELS = ['a', 'e', 'i', 'o', 'u']


    def start_with_vowel(s):
        if s.lower() in VOWELS:
            return True
        else:
            return False

    def minion_game(string):
        global player_a
        global player_b
        length = len(string)
        for i in range(length):
            if start_with_vowel(string[i]):
                player_a = player_a + (length - i)
            else:
                player_b = player_b + (length - i)
        if player_a < player_b:
            print(f"Stuart {player_b}")
        elif player_a == player_b:
            print("Draw")

        else:
            print(f"Kevin {player_a}")