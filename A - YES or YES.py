# A - YES or YES - By: David Bautista - @PipeBau
# url: https://codeforces.com/contest/1703/problem/A

x = int(input())
for i in range(x):
    text = input()
    if text.lower()=='yes':
        print('YES')
    else:
        print('No')
