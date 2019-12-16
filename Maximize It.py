# Maximize It
lin1 = input()
total = 0
k = int(lin1.split()[0])
m = int(lin1.split()[1])

for _ in range(k):
    line = input()
    temp = []
    for i in range(1, int(line.split()[0])+1):
        temp.append( int(line.split()[i]) )
    total += max( temp )**2
    
print( total%m )