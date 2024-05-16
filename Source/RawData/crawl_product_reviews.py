import requests
import json

review_url_template = "https://tiki.vn/api/v2/reviews?limit=1&include=comments&page={}&spid=50685549&product_id={}&seller_id=1"
review_info_file = "product-reviews.txt"
product_id_file = "product-id.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

def crawl_reviews(review_url):
    response = requests.get(review_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to crawl reviews: ", response.status_code)
        return None

def save_review_info(review_info):
    with open(review_info_file, "a", encoding='utf-8') as file:
        file.write(str(review_info) + "\n\n")
    print("Saved review info")

# Đọc giá trị i từ tệp product-id.txt và thực hiện crawl đánh giá cho mỗi giá trị
with open(product_id_file, "r") as id_file:
    for line in id_file:
        i = line.strip()
        print(i)
        page = 1
        while True:
            review_url = review_url_template.format(page, i)
            review_data = crawl_reviews(review_url)
            if review_data and len(review_data["data"]) != 0:
                save_review_info(review_data)
                page += 1
            else:
                i = str(int(i) + 1)
                break
            
        
