import levenshtein

#opens the little women corpus and stores the words in a dictionary
def corpora():
  C = {}
  with open("corpora","r") as myfile:
	for line in myfile:
		words = line[:-1]
		C[words]= 0
  return C



#find5 finds the top 5 edit distances of a word in a corpus. it returns a list of the top 5 closest words in the corpus. 
# The variables are the word (string format) for which we are looking similar words for and the corpus in form of a dictionary with the words as keys.
#@app.route('/search', methods=['GET'])
def find5(word,C):
        #word = request.args.get('q')
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
        return str(top5)
	print(top5)



#if __name__=="__main__":
    #from sys import argv
    #print find5(argv[1],C)
