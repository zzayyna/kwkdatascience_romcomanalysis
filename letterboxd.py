from bs4 import BeautifulSoup
import requests
import pandas as pd

count = 0
data = []
review_text = ""
review_date = ""

for page in range(200):
    url = f'https://letterboxd.com/film/how-to-lose-a-guy-in-10-days/reviews/by/added/page/{page}/'
    response = requests.get(url)
    reviews_page = BeautifulSoup(response.content, "html.parser")
    review_boxes = reviews_page.find_all("div",attrs={'class':'listitem'})
    count+=len(review_boxes)
    for review in review_boxes:
        # text
        review_text_tag = review.find("p")
        review_text = review_text_tag.get_text(strip=True) if review_text_tag else ""

        # date
        review_date_tag = review.find("time", attrs={'class':'timestamp'})
        review_date = review_date_tag.get_text(strip=True) if review_date_tag else ""
    
        data.append([review_text,review_date])

df = pd.DataFrame(data, columns=["Review Text", "Date"])
df.to_csv("letterboxd_reviews.csv", index=False, encoding="utf-8-sig")

print("scraped " + str(count)+ " reviews, scraping complete")
