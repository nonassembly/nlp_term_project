import hanja
from hanja import hangul
from collections import Counter
import re

from konlpy.tag import Twitter
nlpy = Twitter()
nouns = nlpy.nouns(lines)

count = Counter(nouns)

INPUT_FILE='./each_100thousand.csv'
OUTPUT_FILE='cleaned_data.csv'

def clean_text(text):
    
    cleaned_text = re.sub('[a-zA-z]','',text)
    cleaned_text = re.sub('[\{\}\[\]\/?.;:|\())*~`!^\-_+<>@\#$%&]','',cleaned_text)
    print(text[0])
    print(text[20399338])
    i=0
    while(text[i] is True):
        trans=hangul.is_hangul(text[i])
        if trans==True:
            y=hanja.translate('trans','substitution')
            text.maketrans('trans', y)
        i+=1
        print(i)
    return cleaned_text

def count_text(text):

    tag_count = []
    tags = []
    for n, c in count.most_common(100000):
        dics = {'tag': n, 'count': c}
    if len(dics['tag']) >= 2 and len(tags) <= 49:
        tag_count.append(dics)
        tags.append(dics['tag'])
        
        
    for tag in tag_count:
        print(" {:<14}".format(tag['tag']), end='\t')
        print("{}".format(tag['count']))



read_file = open(INPUT_FILE,'r', encoding='euc-kr')
write_file = open(OUTPUT_FILE,'w', encoding='euc-kr')
text = read_file.read()
text = clean_text(text)
text = count_text(text)
write_file.write(text)
read_file.close()
write_file.close()
    