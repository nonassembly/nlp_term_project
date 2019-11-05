from urllib.request import urlopen
from bs4 import BeautifulSoup

for k in range(1, 12):
	if(k<10):
		stK=k
		k=str('0')+str(k)
	for j in range(1, 31):
		if(j<10):
			stJ=j
			j=str('0')+str(j)
		for i in range(1, 10):
			
			url = "https://news.naver.com/main/list.nhn?mode=LS2D&sid2=264&sid1=100&mid=shm&date=2019"+str(k)+str(j)+"&page="+str(i)
			html = urlopen(url)
			source = html.read() # 바이트코드 type으로 소스를 읽는다.
			html.close() # urlopen을 진행한 후에는 close를 한다.
			soup = BeautifulSoup(source, "html5lib") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름
			soup=soup.find_all('dt')
			print(url)
			for news in soup:
				if(news.a.string!=None):
					print(news.a.string)
		j=stJ
	k=stK