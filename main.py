from bs4 import BeautifulSoup
import sys

with open('test.html') as f:
    soup = BeautifulSoup(f, 'html.parser')


code = soup.find_all('div', class_='ace_layer ace_text-layer')

if len(sys.argv) == 1:
    code = code[0].find_all('div', class_='ace_line')
else:
    code = code[int(sys.argv[1])].find_all('div', class_='ace_line')

with open('out.txt', 'w') as f:
    for i in code:
        f.write(i.text+'\n')
        print(i.text)
