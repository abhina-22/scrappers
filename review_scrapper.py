from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.getyourguide.co.uk/activity/bali-l347/mount-batur-small-group-sunrise-trekking-t249432?utm_force=0'
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")
reviewsArr = []
for review in content.findAll('div', attrs={"class": "review-card__container"}):
    reviewObject = {
        "author": review.find('div', attrs={"class": "review-card__author-details"}).text.replace('\n', ''),
        "date": review.find('p', attrs={"class": "review-card__additional-info-date"}).text,
        "comment": review.find('p', attrs={"class": "review-card__description"}).text,
    }
    reviewsArr.append(reviewObject)
with open('reviews.json', 'w') as outfile:
    json.dump(reviewsArr, outfile)

