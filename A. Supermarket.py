# A. Supermarket - By: David Bautista - @PipeBau
#url: https://codeforces.com/problemset/problem/919/A

n,k = [int(i) for i in input().split(' ')]
values = []
for j in range(n):
  a,b = [int(i) for i in input().split(' ')]
  values.append(a/b)
print(min(values)*k)
