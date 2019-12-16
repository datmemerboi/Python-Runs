line1 = input()
line2 = input()

def replacer(word, repetition):
	for spl in line2.split():
		letters=[]; rep={};
		for j in range(len(spl)):
			if( spl[j] in letters):
				if(spl[j] not in rep.keys()):
					rep[spl[j]]=2
				else:
					rep[spl[j]]=rep[spl[j]]+1
			else:
				letters.append(spl[j])
		if(rep!={} and rep==repetition):
			global line1
			line1 = line1.replace(word, spl)


for spl in line1.split():
	letters=[]; rep={};
	for i in range(len(spl)):
		if( spl[i] in letters):
			if(spl[i] not in rep.keys()):
				rep[spl[i]]=2
			else:
				rep[spl[i]]=rep[spl[i]]+1
		else:
			letters.append(spl[i])
	replacer(spl, rep)
print(line1)
line1=line2=None