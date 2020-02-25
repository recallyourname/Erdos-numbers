listOfArticles = []
dictOfAuthors = {}
listOfAuthors = []
checkList = []

def initErdos():
	for article in listOfArticles:
		for key in dictOfAuthors.keys():
			for author in listOfAuthors:
				if key in article and "Erdos" in article:
					dictOfAuthors[key] = 1
				if (key in article) and (author in article) and dictOfAuthors[author] > 0 and author != "Erdos" and dictOfAuthors[key] == 0:
					dictOfAuthors[key] = dictOfAuthors[author] + 1
	for key in dictOfAuthors:
		if dictOfAuthors[key] == 0:
			dictOfAuthors[key] = 'infinity'
			
def articleParser(listElement):
	name = ""
	ch = ""
	for ch in listElement:
		if (ch == ":"):
			break
		elif (ch != " ") and (ch != ","):
			name += ch
		else:
			if name not in (dictOfAuthors and listOfAuthors) and (name != ""):
				dictOfAuthors.update({name : 0})
				listOfAuthors.append(name)
				name = ""
			elif name in (dictOfAuthors and listOfAuthors):
				name=""		

def articleInput(num):
	print("Scenario ", num, end="\n")
	p = int(input("Input the number of articles: "))
	for i in range(p):
		listOfArticles.append(input("Input the data of article (format: 'surname, surname : article'): "))
	for article in listOfArticles:
		articleParser(article)

def main():
	n = int(input("Input the number of scenarios: "))
	for i in range(n):
		articleInput(i+1)
		initErdos()
		p = int(input("Input the number of authors you want to check: "))
		for _ in range(p):
			checkList.append(input("Input the surname of author you want to check: "))
		for author in checkList:
			print(dictOfAuthors[author])	
		print(dictOfAuthors)
		print(listOfAuthors)

if __name__ == '__main__':
	main()