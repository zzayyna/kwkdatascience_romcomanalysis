from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#create a chrome service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.rottentomatoes.com/m/how_to_lose_a_guy_in_10_days/reviews?type=user')
driver.implicitly_wait(10)

#keep clicking load more until end of page, avoid timeouts if loading takes to long
count = 0
while True:
    try:
        load_more = WebDriverWait(driver, 10000 ).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="load-more-btn"]'))
        )
        driver.execute_script("arguments[0].click();", load_more)

        WebDriverWait(driver, 10000).until(
            lambda d: len(d.find_elements(By.CLASS_NAME, "audience-review-row")) > count
        )

        # update counter
        count = len(driver.find_elements(By.CLASS_NAME, "audience-review-row"))
        print(f"Loaded {count} reviews so far...")

    except Exception:
        print("No more reviews or button not clickable within timeout.")
        break

#collect all reviews
reviews = driver.find_elements(By.CLASS_NAME, "audience-review-row")
print(f"Total reviews loaded: {len(reviews)}")

#add reviews to array
data = []
for review in reviews:  
    review_text = review.find_element(By.CLASS_NAME, "audience-reviews__review").text.strip()
    review_date = review.find_element(By.CLASS_NAME, "audience-reviews__duration").text.strip()
    rating_elem = review.find_element(By.TAG_NAME, "rating-stars-group")
    review_rating = rating_elem.get_attribute("score")
    data.append([review_text,review_date,review_rating])

#save reviews to csv file
df = pd.DataFrame(data, columns=["Review Text", "Date", "Rating"])
df.to_csv("rottentomatoes_reviews2.csv", index=False, encoding="utf-8-sig")

print("scraping complete")

driver.quit()

