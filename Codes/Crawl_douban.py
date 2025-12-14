import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
movies = soup.find('ol', class_='grid_view').find_all('li')

for movie in movies:
    title = movie.find('div', class_='pic').find('span', class_='title').get_text()
    rating_num = movie.find('div', class_='star').find('span', class_='rating_num').get_text()
    comment_num = movie.find('div', class_='star').find_all('span')[-1].get_text()
    print(title, rating_num, comment_num)
    