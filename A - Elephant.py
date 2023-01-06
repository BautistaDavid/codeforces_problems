# A - Elephant - By: David Bautista - @PipeBau
# url: https://codeforces.com/contest/617/problem/A

n = int(input())
cont = 0
if n%5 == 0:
  cont+=n/5
for i in range(1,5):
  if (n-i)%5 ==0:
    n_1=(n-i)/5
    cont+=n_1
    if n_1 == 4:
      cont+=2
    if n_1 != 4:
      cont+=1
print(int(cont))
