import requests
from bs4 import BeautifulSoup
from playlist import Playlist

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD:')
URL = f'https://www.billboard.com/charts/hot-100/{date}/'
year = date.split('-')[0]

response = requests.get(url=URL)
billboard_webPg = response.text

soup = BeautifulSoup(billboard_webPg, 'html.parser')
top_song_tag = soup.find('h3')
top_song = ' '.join(top_song_tag.getText().split())
song_tags = soup.find_all('h3', id='title-of-a-story', class_='c-title a-no-trucate a-font-primary-bold-s u-letter'
                                                              '-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-'
                                                              '16 u-line-height-125 u-line-height-normal@mobile-max a-'
                                                              'truncate-ellipsis u-max-width-330 '
                                                              'u-max-width-230@tablet-'
                                                              'only')
song_list = [' '.join(tag.getText().split()) for tag in song_tags]
song_list.insert(0, top_song)

play_list = Playlist(songs_name=song_list, year=year, date=date)
