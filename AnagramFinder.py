# NUMBER OF ANAGRAMS FINDER

def countSentences(wordSet, sentences):
	intArray = []
	NotHere = True
	for _ in sentences:
		sent = _.split()
		counter = 0
		for i in sent:
			for j in wordSet:
				if(len(i) == len(j)):
					word1 = [word for word in i]
					word2 = [word for word in j]
					for k in word1:
						if(k not in word2):
							NotHere = True
							break
						else:
							NotHere = False
						if(not(NotHere)):
							counter+=1
							break
		intArray.append(counter)
	return(intArray)


if __name__ == '__main__':
	WordSetLen = int(input())
	wordSet = []
	for _ in range(WordSetLen):
		wordSet.append(input())

	SentencesLen = int(input())
	sentences = []
	for _ in range(SentencesLen):
		sentences.append(input())
	print( wordSet, sentences)

	print(countSentences(wordSet, sentences))