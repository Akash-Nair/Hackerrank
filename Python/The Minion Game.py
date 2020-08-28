
def minion_game(string):
    # your code goes here
    n = len(string)
    kevin = 0
    stuart = 0
    vowel = 'AEIOU'
    for i in range(n):
        if string[i] in vowel:
            kevin+=n-i
        else:
            stuart+=n-i

    if stuart>kevin:
        print('Stuart',stuart)
    elif stuart<kevin:
        print('Kevin',kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
