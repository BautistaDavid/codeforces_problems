# codigo BIT++ by:David Bautista - @PipeBau
# url: https://codeforces.com/contest/282/problem/A
n= int(input(""))     
output = 0                    
for i in range(n):     
  op= input("")
  if op[1] == "+":         
    output+=1
  if op[1] == "-":        
    output-=1
print(output)   
