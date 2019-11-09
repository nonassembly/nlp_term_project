from konlpy.tag import Okt
import csv
import operator
okt=Okt()

INPUT_FILE='cleaned_data.csv'
OUTPUT_FILE='data_dic.txt'
dic={}
with open(INPUT_FILE, newline='') as csvfile:
		text=csv.reader(csvfile, delimiter=',')
		for title in text:
			title=okt.morphs(title[0])
			for word in title:
				if word not in dic.keys():
					dic[word]=1
				else:
					dic[word]+=1

dic=sorted(dic.items(), key=lambda x: x[1], reverse=True)
with open(OUTPUT_FILE, 'w') as datafile:
	for data in dic:
		datafile.write(data[0]+' '+str(data[1])+'\n')