import levenshtein

#opens the little women corpus and stores the words in a dictionary
def corpora():
  C = {}
  with open("corpora","r") as myfile:
    for line in myfile:
	words = line[:-1]
	C[words]= 0
  return C

#opens the animal list and stores the words in a dictionary
#D = {}
#with open("Animal List","r") as myfile:
#	for line in myfile:
#		words = line[:-1]
#		D[words.lower()]= 0

#opens list of collocations
Collocs = {}
with open("collocations","r") as myfile:
	for line in myfile:
		elements = line[:-1].split()
		words = elements[0] + " " + elements[1]
		print(words)
		Collocs[words]= int(elements[2])

#find5 finds the top 5 edit distances of a word in a corpus. it returns a list of the top 5 closest words in the corpus. 
# The variables are the word (string format) for which we are looking similar words for and the corpus in form of a dictionary with the words as keys.
def find5(word,corpus):
	minimum = len(word)
	top5 = ["","","","",""]
	edit_dist5 = [minimum]*5
	

	for c in C:
		edit_dist = levenshtein.levenshtein(word,c)
		#print(edit_dist)
		if edit_dist > edit_dist5[4]:
			continue
		elif edit_dist == 0:
			continue
		elif edit_dist < edit_dist5[0]:
			edit_dist5= [edit_dist] + edit_dist5[:4]
			top5= [c] + top5[:4]
		elif edit_dist < edit_dist5[1]:
			edit_dist5= [edit_dist5[0]] + [edit_dist] + edit_dist5[1:4]
			top5= [top5[0]] + [c] + top5[1:4]
		elif edit_dist < edit_dist5[2]:
			edit_dist5= edit_dist5[:2] + [edit_dist] + edit_dist5[2:4]
			top5= top5[:2] + [c] + top5[2:4]
		elif edit_dist < edit_dist5[3]:
			edit_dist5= edit_dist5[:3] + [edit_dist] + [edit_dist5[3]]
			top5= top5[:3] + [c] + [top5[3]]
		elif edit_dist < edit_dist5[4]:
			edit_dist5= edit_dist5[:4] + [edit_dist]
			top5= top5[:4] + [c]
	return top5
	print(top5)

def find10(word,corpus):
	minimum = len(word)
	top10 = ["","","","","","","","","",""]
	edit_dist10 = [minimum]*10
	

	for c in C:
		edit_dist = levenshtein.levenshtein(word,c)
		#print(edit_dist)
		if edit_dist > edit_dist10[4]:
			continue
		elif edit_dist == 0:
			continue
		elif edit_dist < edit_dist10[0]:
			edit_dist5= [edit_dist] + edit_dist10[:9]
			top10= [c] + top10[:9]
		elif edit_dist < edit_dist10[1]:
			edit_dist10= [edit_dist10[0]] + [edit_dist] + edit_dist10[1:9]
			top10= [top10[0]] + [c] + top10[1:9]
		elif edit_dist < edit_dist10[2]:
			edit_dist10= edit_dist10[:2] + [edit_dist] + edit_dist10[2:9]
			top10= top10[:2] + [c] + top10[2:9]
		elif edit_dist < edit_dist10[3]:
			edit_dist10= edit_dist10[:3] + [edit_dist] + edit_dist10[3:9]
			top10= top10[:3] + [c] + top10[3:9]
		elif edit_dist < edit_dist10[4]:
			edit_dist5= edit_dist10[:4] + [edit_dist] + top10[4:9]
			top10= top10[:4] + [c] + top10[4:9]
		elif edit_dist < edit_dist10[5]:
			edit_dist10= edit_dist10[:5] + [edit_dist] + edit_dist10[5:9]
			top10= top10[:5] + [c] + top10[5:9]
		elif edit_dist < edit_dist10[6]:
			edit_dist10= edit_dist10[:6] + [edit_dist] + edit_dist10[6:9]
			top10= top10[:6] + [c] + top10[6:9]
		elif edit_dist < edit_dist10[7]:
			edit_dist10= edit_dist10[:7] + [edit_dist] + edit_dist10[7:9]
			top10= top10[:7] + [c] + top10[7:9]
		elif edit_dist < edit_dist10[8]:
			edit_dist10= edit_dist10[:8] + [edit_dist] + edit_dist10[8:9]
			top10= top10[:8] + [c] + top10[8:9]
		elif edit_dist < edit_dist10[9]:
			edit_dist10= edit_dist10[:-1] + [edit_dist]
			top10= top10[:-1] + [c]
	return top10
	print(top10)

def choosecolloc5(list1,list2):
	possiblecollocs = []
	for word1 in list1:
		for word2 in list2:
			collocwords = word1 + " " + word2
			if collocwords in Collocs.keys():
				collocvalue = Collocs[collocwords]
				possiblecollocs += [(collocvalue,collocwords)]
			else:
				possiblecollocs += [(0,collocwords)]

	sortedcollocs = sorted(possiblecollocs, key=lambda tup: tup[0])
	return sortedcollocs[:5]

#create 5 takes the words from dictionary D (here animal list) to make
def create5(name):
	f = open(name,"w")
	
	for word in D:
		f.write(word + "\n")
		words5 = find5(word,C)
		for w in words5:
			f.write(w + " ")
		f.write("\n")

	f.close()

if __name__=="__main__":
    from sys import argv
    if " " not in argv[1]:
    	print find5(argv[1],C)
    else:
    	words = argv[1].split(" ",1)
    	list1 =  find10(words[0],C)
    	list2 =  find10(words[1],C)
    	print(list1)
    	print(list2)
    	print(choosecolloc5(list1,list2))



