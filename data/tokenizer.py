from konlpy.tag import Okt, Kkma, Mecab
import csv

okt=Okt()
kkma=Kkma()
mecab=Mecab()

dic1={}
dic2={}
dic3={}

news_title1=[]
news_title2=[]
news_title3=[]

count=0
with open('cleaned_data.csv', newline='', encoding='euc-kr') as csvfile:
	text=csv.reader(csvfile, delimiter=',')
	for title in text:
		news_title=okt.nouns(title[0])
		news_title1.append(news_title)
		for word in news_title:
			if word not in dic1.keys():
				dic1[word]=1
			else:
				dic1[word]+=1

		news_title=kkma.nouns(title[0])
		news_title2.append(news_title)
		for word in news_title:
			if word not in dic2.keys():
				dic2[word]=1
			else:
				dic2[word]+=1

		news_title=mecab.nouns(title[0])
		news_title3.append(news_title)
		for word in news_title:
			if word not in dic3.keys():
				dic3[word]=1
			else:
				dic3[word]+=1
		
		count+=1		
		print(count)

dic1=sorted(dic1.items(), key=lambda x: x[1], reverse=True)
with open('dic_okt.txt', 'w') as datafile:
	for data in dic1:
		datafile.write(data[0]+' '+str(data[1])+'\n')

dic2=sorted(dic2.items(), key=lambda x: x[1], reverse=True)
with open('dic_kkma.txt', 'w') as datafile:
	for data in dic2:
		datafile.write(data[0]+' '+str(data[1])+'\n')

dic3=sorted(dic3.items(), key=lambda x: x[1], reverse=True)
with open('dic_mecab.txt', 'w') as datafile:
	for data in dic3:
		datafile.write(data[0]+' '+str(data[1])+'\n')