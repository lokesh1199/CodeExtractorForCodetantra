from bs4 import BeautifulSoup

with open('test.html') as f:
    soup = BeautifulSoup(f, 'html.parser')


code = soup.find_all('div', class_='ace_layer ace_text-layer')

if len(code[0]):
    code = code[0].find_all('div', class_='ace_line')
else:
    code = code[1].find_all('div', class_='ace_line')

with open('out.txt', 'w') as f:
    for i in code:
        f.write(i.text+'\n')
        print(i.text)
