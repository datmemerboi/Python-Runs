# XYZ OCCURANCE CHECK
def xyzReplace(String):
	finalCount = 0
	if ("xy" in String) or ("yx" in String):
		finalCount += 1
	if ("yz" in String) or ("zy" in String):
		finalCount += 1
	if ("xz" in String) or ("zx" in String):
		finalCount += 1
	return(finalCount)

String  = input("Enter:")

answer = xyzReplace(String)
print(answer)