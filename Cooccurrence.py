import re

S = []
with open("stopwords","r") as myfile:
		for line in myfile:
			word = line[:-1]
			S+=[word]

#print(S.keys())
#measures cooccurrence of words based on collocations
def cooccur(texts,name):
	C ={}
	T = {}
	with open(texts,"r") as myfile:
		lastword = "begin"
		for line in myfile:
			words = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+",line)
			wordes = []
			for word in words:
				if word in S:
					#print(word)
					continue
				if not(word.isdigit() or (word[-1:]=="-") or (word[:1]=="-") or (word[:1]=="\'")): 
					wordes += [word.lower()]
			i = 1
			
			for word in wordes:
				if i== len(wordes):
					lastword = wordes[-1]
					break
				word2 = wordes[i]
				collocation = word + " " + word2
				if collocation in C.keys():
					C[collocation] = C[collocation] + 1
				else:
					C[collocation] = 1
				i+= 1

	f = open(name,"w")
	for colloc in C:
		f.write(colloc + " " + str(C[colloc]) +  "\n")

	f.close()