# FIND LUCKY NUMBERS BETWEEN NUMBERS PROVIDED IN INPUT LINE
def LuckyNum(a, b):
	finalCount = 0
	NotPrime = False
	for i in range(a, b+1):
		x = []
		x2 = []
		for p in range(0, len( str(i) ) ):
			x.append( int(str(i)[p]) )
			x2.append( int(str(i)[p])**2 )
			Sum1 = sum(x)
			Sum2 = sum(x2)
			for q in range(2, Sum1):
				if( Sum1%q==0):
					NotPrime = True
			for q in range(2, Sum2):
				if(Sum2%q==0):
					NotPrime = True
		if( not(NotPrime) ):
		finalCount+=1

	print(finalCount)

line = input("Enter as line:")
a = int( line.split()[0] )
b = int( line.split()[1] )
LuckyNum(a,b)