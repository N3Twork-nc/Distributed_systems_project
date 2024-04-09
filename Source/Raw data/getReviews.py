import requests
import pandas as pd

url = "https://tiki.vn/api/v2/reviews?limit=5&include=comments,contribute_info,attribute_vote_summary&sort=stars%7C5&page={}&spid=50685549&product_id={product_id}&seller_id=1"

product_id_file = "product-id.txt"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

# Lấy dữ liệu từ tất cả các trang
all_reviews = []

def crawl_reviews():
    

