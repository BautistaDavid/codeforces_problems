# A - Helpful Maths. - By: David Bautista - @PipeBau
# url: 

x = input()
x = [int(i)for i in x.split("+")]
x.sort()
y = ""
for j in x:
  y+=str(f"{j}+") 
print(y.rstrip("+"))
