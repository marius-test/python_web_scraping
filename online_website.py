from bs4 import BeautifulSoup
import requests


response = requests.get('https://fr.jooble.org/SearchResult?loc=2&rgns=Ile-de-France&ukw=qa+engineer').text
soup = BeautifulSoup(response, 'lxml')

articles = soup.find_all('article', class_='FxQpvm yKsady')

for article in articles:
    matches = ['jour', 'jours', 'heure', 'heures']
    date_published = article.find('div', class_='caption e0VAhp').text

    if any(x in date_published for x in matches):
        job = article.find('a', class_='jkit__4ouL4 jkit__300pp hyperlink_appearance_undefined jkit__3uS8R _2dWEc6').text
        company = article.find('p', class_='Ya0gV9').text
        location = article.find('div', class_='caption _2_Ab4T').text
        remote = article.find('div', class_='_2Hplhb').text

        if remote in ['Travail à distance', 'Télétravail']:
            remote_status = 'Yes'
        else:
            remote_status = 'No'

        print(f'Company name: {company}')
        print(f'Role: {job}')
        print(f'Location: {location}')
        print(f'Remote: {remote_status}')
        print(f'Date published: {date_published[1:]}\n')
