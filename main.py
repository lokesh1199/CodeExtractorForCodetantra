from bs4 import BeautifulSoup

with open('test.html') as f:
    soup = BeautifulSoup(f, 'html.parser')


code = soup.find('div', class_='ace_layer ace_text-layer')

code = code.find_all('div', class_='ace_line')

with open('out.txt', 'w') as f:
    for i in code:
        f.write(i.text+'\n')
        print(i.text)
