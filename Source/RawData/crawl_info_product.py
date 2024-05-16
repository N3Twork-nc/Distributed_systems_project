import requests
import json

product_url_template = "https://tiki.vn/api/v2/products/{}?platform=web&spid={}&version=3"
product_info_file = "product-info.txt"
product_id_file = "product-id.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

def crawl_product(product_url):
    response = requests.get(product_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to crawl product: ", response.status_code)
        return None

def save_product_info(product_info):
    with open(product_info_file, "a", encoding='utf-8') as file:
        file.write(json.dumps(product_info) + "\n\n")
    print("Saved product info")

try:
    # Đọc giá trị i từ tệp product-id.txt và thực hiện crawl cho mỗi giá trị
    with open(product_id_file, "r") as id_file:
        for line in id_file:
            i = line.strip()
            print(i)
            product_url = product_url_template.format(i, i)
            product_info = crawl_product(product_url)
            if product_info:
                save_product_info(product_info)
except FileNotFoundError:
    print("File 'product-id.txt' not found. Please make sure the file exists.")
except Exception as e:
    print("An error occurred:", e)
