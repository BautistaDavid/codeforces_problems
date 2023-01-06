# A. Petya and Strings - By: David Bautista - @PipeBau
# url: https://codeforces.com/contest/112/problem/A

w_1=input("")
w_2=input("")
if w_1.lower() > w_2.lower():
  print(1)
if w_1.lower() < w_2.lower():
  print(-1)
if w_1.lower() == w_2.lower():
  print(0)
