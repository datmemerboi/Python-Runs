# TCS Question
x = y = 0
n = int(input())
for i in range(1, n+1):
    if i%4==1:
        x = x+(10*i)
    if i%4==2:
        y = y+(10*i)
    if i%4==3:
        x = x-(10*i)
    if i%4==0:
        y = y-(10*i)
print(x, y)