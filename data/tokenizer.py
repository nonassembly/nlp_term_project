from konlpy.tag import Okt, Kkma
import csv

okt=Okt()
kkma=Kkma()

dic=[{},{},{},{}]
news_title=[[],[],[],[]]
count=0
with open('cleaned_data.csv', newline='') as csvfile:
		text=csv.reader(csvfile, delimiter=',')

		for title in text:
			news_title[0].append(okt.morphs(title[0]))
			news_title[1].append(okt.nouns(title[0]))
			news_title[2].append(kkma.nouns(title[0]))

			for i in range(0, 3):
				for news in news_title[i]:
					for word in news:
						if word not in dic[i].keys():
							dic[i][word]=1
						else:
							dic[i][word]+=1
			count+=1
			print(count)

for i in range(0, 3):			
	dic[i]=sorted(dic[i].items(), key=lambda x: x[1], reverse=True)
	with open('dictionary'+str(i)+'.txt', 'w') as datafile:
		for data in dic[i]:
			datafile.write(data[0]+' '+str(data[1])+'\n')