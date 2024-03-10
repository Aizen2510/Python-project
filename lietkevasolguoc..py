n = int(input())
diem =0
for i in range(1, n+1):
    if n%i==0:
      diem +=1
print(diem)

for i in range(1, n+1):
    if n%i==0:
      print(i, end=" ")