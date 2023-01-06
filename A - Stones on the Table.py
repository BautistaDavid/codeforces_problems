# A - Stones on the Table - By: David Bautista - @PipeBau
# url: https://codeforces.com/contest/266/problem/A

n_stones = int(input())
stones = list(input())
cont = 0
idx = 0
for stone in stones[:-1]:
  if stone == stones[idx+1]:
    cont +=1
  else:
    None
  idx +=1
print(cont)
