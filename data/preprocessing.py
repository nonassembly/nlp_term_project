import re

INPUT_FILE='./each_100thousand.csv'
OUTPUT_FILE='cleaned_data.csv'

def clean_text(text):
    cleaned_text = re.sub('[a-zA-z]','',text)
    cleaned_text = re.sub('[\{\}\[\]\/?.;:|\())*~`!^\-_+<>@\#$%&]','',cleaned_text)
    return cleaned_text

read_file = open(INPUT_FILE,'r', encoding='euc-kr')
write_file = open(OUTPUT_FILE,'w', encoding='euc-kr')
text = read_file.read()
text = clean_text(text)
write_file.write(text)
read_file.close()
write_file.close()
    