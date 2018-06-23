def feels(sentiment):
	sad=[];disgust=[];anger=[];anticipation=[];
	fear=[];enjoyment=[];trust=[];surprise=[];
	#open 8 files with 8 emotion data sets - each emotion file has an array of words pertaining to that emotion
	file=open('sad.txt','r')
	contents=file.readlines()
	for line in contents:
		for word in line.split(", "):
			sad.append(word.lower())
	file1=open('disgust.txt','r')
	contents=file.readlines()
	for line in contents:
		for word in line.split(", "):
			disgust.append(word.lower())
	file2=open('anger.txt','r')
	contents=file.readlines()
	for line in contents:
		for word in line.split(", "):
			anger.append(word.lower())
	file3=open('anticipation.txt','r')
	contents=file.readlines()
	for line in contents:
		for word in line.split(", "):
			anticipation.append(word.lower())
	file4=open('fear.txt','r')
	contents=file.readlines()
	for line in contents:
		for word in line.split(", "):
			fear.append(word.lower())
	file5=open('enjoyment.txt','r')
	contents=file.readlines()
	for line in contents:
		for word in line.split(", "):
			enjoyment.append(word.lower())
	file6=open('trust.txt','r')
	contents=file.readlines()
	for line in contents:
		for word in line.split(", "):
			trust.append(word.lower())
	file7=open('surprise.txt','r')
	contents=file.readlines()
	for line in contents:
		for word in line.split(", "):
			surprise.append(word.lower())
	sad.append("sad")
	disgust.append("disgust")
	anger.append("anger")
	anticipation.append("anticipation")
	fear.append("fear")
	enjoyment.append("enjoyment")
	trust.append("trust")
	surprise.append("surprise")
	#search if a particular emotion is in the given lists
	if sentiment in sad:
		return "sad"
	elif sentiment in disgust:
		return "disgust"
	elif sentiment in anger:
		return "anger"
	elif sentiment in anticipation:
		return "anticipation"
	elif sentiment in fear:
		return "fear"
	elif sentiment in enjoyment:
		return "enjoyment"
	elif sentiment in trust:
		return "trust"
	elif sentiment in surprise:
		return "surprise"	
#check if files are being used correctly by a driver
#print feels("miracle")