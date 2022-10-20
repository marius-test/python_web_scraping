from bs4 import BeautifulSoup
import requests
from time import sleep


def find_jobs():
    response = requests.get('https://fr.jooble.org/SearchResult?loc=2&ukw=qa+engineer').text
    soup = BeautifulSoup(response, 'lxml')

    articles = soup.find_all('article', class_='FxQpvm yKsady')
    for index, article in enumerate(articles):

        matches = ['jour', 'jours', 'heure', 'heures']
        date_published = article.find('div', class_='caption e0VAhp').text
        if any(x in date_published for x in matches):

            job = article.find('a', class_='jkit__4ouL4')
            company = article.find('p', class_='Ya0gV9').text
            location = article.find('div', class_='caption _2_Ab4T').text

            remote = article.find('div', class_='_2Hplhb').text
            if remote in ['Travail à distance', 'Télétravail']:
                remote_status = 'Yes'
            else:
                remote_status = 'No'

            with open(f'files/{index}.txt', 'w') as f:
                f.write(f'Company name: {company}\n')
                f.write(f'Role: {job.text}\n')
                f.write(f'Location: {location}\n')
                f.write(f'Remote: {remote_status}\n')
                f.write(f'Date published: {date_published[1:]}\n')
                f.write(f"More info: {job['href']}")

            print(f'File saved as {index}.txt')


if __name__ == '__main__':
    while True:
        find_jobs()
        minutes = 1440
        print(f'Waiting {minutes} minutes...')
        sleep(minutes * 60)
