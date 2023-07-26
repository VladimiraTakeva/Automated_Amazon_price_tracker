from bs4 import BeautifulSoup
import requests
import smtplib
import os
my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "bg-BG,bg;q=0.9,en;q=0.8",
}
response = requests.get("https://www.amazon.com/Instant-Pot-Ultimate-Pressure-Dehydrate/dp/B0B1G5M31V/ref=sr_1_4?crid=3DQXXE4JKWQKB&keywords=instant%2Bpot%2Band%2Bair%2Bfryer%2Bcombo&qid=1685008254&sprefix=Instant%2BPot%2B%2Band%2B%2Caps%2C184&sr=8-4&th=1", headers=headers)
amazon_web = response.content

# print(amazon_web)

soup = BeautifulSoup(amazon_web, "html.parser")
title = soup.find(id="productTitle").get_text().strip()
price = soup.find(class_="a-offscreen").getText()
url = "https://www.amazon.com/Instant-Pot-Ultimate-Pressure-Dehydrate/dp/B0B1G5M31V/ref=sr_1_4?crid=3DQXXE4JKWQKB&keywords=instant%2Bpot%2Band%2Bair%2Bfryer%2Bcombo&qid=1685008254&sprefix=Instant%2BPot%2B%2Band%2B%2Caps%2C184&sr=8-4&th=1"
price = float(price.replace("$", ""))

if price < 150:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vl.takeva@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{title} is now ${price}.You can check here:\n{url}".encode("utf-8"))
