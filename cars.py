# pip install -r requirements.txt
import requests

from bs4 import BeautifulSoup

URL = "https://cars.kg/offers"
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "accept": "*/*",
}

def get_html(url, headers):
    response = requests.get(url, headers=headers)
    return response
def get_content_from_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    items = soup.find_all("a", class_="catalog-list-item")
    laptops = []
    for item in items:
        laptops.append(
            {
                "imge":item.find("img").get("src"),
                "title": item.find("span", class_="catalog-item-params").get_text().replace("\n", ""),
                "milage": item.find("span", class_="catalog-item-mileage").get_text().replace("\n", ""),
                "caption": item.find("span", class_="catalog-item-caption").get_text().replace("\n", ""),
                "year": item.find("span", class_="caption-year").get_text().replace("\n", ""),
                "price": item.find("span", class_="catalog-item-price").get_text().replace("\n", ""),
                "price-som": item.find(int("span", "catalog-item-price").get_text().replace("\n", "").find("catalog-item-price"[0:-1]) * 83),
                "descr": item.find("span", class_="catalog-item-descr").get_text().replace("\n", ""),
            }
        )
    print(laptops)

def get_result_parse():
    html = get_html(URL, HEADERS)
    if html.status_code == 200:
        get_content_from_html(html.text)

get_result_parse()