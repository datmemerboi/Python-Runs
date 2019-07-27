# JSON Syntax
InpStr = input("Enter string to check: ")
balanced = depth = 0

for i in range(0, len(InpStr)):
	if(InpStr[i]=='[' or InpStr[i]=='{'):
		balanced += 1
		depth += 1
	if(InpStr[i]==']' or InpStr[i]=='}'):
		balanced -= 1
		
print( not(bool(balanced)) )
print(depth)