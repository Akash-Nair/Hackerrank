def print_rangoli(size):
    # your code goes here
    width = 4*size-3 
    bottom = []
    for i in range(0,size):
        s = chr(96+size)
        for j in range(size-1,size-i-1,-1):
            s = s + '-' + chr(96+j)
        x = s[:-1]
        x = x[::-1]
        s = s + x
        bottom.append(s)
        print(s.center(width,'-'))

    bottom = bottom[:-1]
    for i in bottom[::-1]:
        print(i.center(width,'-'))
    

    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
