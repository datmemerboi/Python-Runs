# For a given size and elements of a list,
# swap the list item with the corresponding array Index
n = int(input())
line = input().split()

arr = []
for i in range(n):
	arr.append( int(line[i]) )

swap = []
for i in range(n):
	swap.append( [ i, arr[i] ] )

for i in range(n):
	arr[ swap[i][1] ] = int(i)

Str = ""
for i in arr:
	if(len(Str)==0):
		Str += str(i)
	else:
		Str += " "+str(i)
print(Str.strip() )