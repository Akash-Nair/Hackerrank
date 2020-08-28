from collections import defaultdict
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        s = string[i:i+k]
        ans = ''
        d = defaultdict(int)
        for j in range(len(s)):
            if d[s[j]] == 0:
                d[s[j]] = 1
                ans+=s[j]
        print(ans)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
