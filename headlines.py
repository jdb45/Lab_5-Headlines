from bs4 import BeautifulSoup
import datetime
import requests
now = datetime.datetime.now()
# getting the URL for the website
html = 'http://www.espn.com/'
# opening the website
r = requests.get(html)
# parsing the information
soup = BeautifulSoup(r.text, 'html.parser')
list = []
# searching for the headlines and displaying them
for headline in soup('span', {'class' : 'headline'}):
    print('*', headline.text, '\n')
    list.append(headline.text)

# getting the date and time
list.append(now.strftime("%Y-%m-%d %H:%M"))
print (now.strftime("%Y-%m-%d %H:%M"))

file = open('output.txt', 'w')
# saving to the file
for l in list:
    file.write("%s\n" % l)

file.close()