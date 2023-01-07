
# B. Decoding - By: David Bautista - @PipeBau
# url:https://codeforces.com/problemset/problem/746/B
 
n = int(input())
word = list(input())
final_word = []
if n <= 2:
  final_word = ''.join(word)
elif n >2:
  for _,i in enumerate(word):
    if _%2 == 0:
      final_word.insert(0,i)
    else:
      final_word.append(i)
  if n%2 == 0:
    final_word = ''.join(final_word)
  else:
    final_word.reverse()
    final_word = ''.join(final_word)
print(final_word)
 
