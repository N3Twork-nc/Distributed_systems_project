import requests
import json

page_url = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&version=home-persionalized&trackity_id=680c18ed-7be4-1045-443b-c3b0e7083ee1&category=8322&page={}&urlKey=nha-sach-tiki"

product_id_file = "product-id.txt"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

def crawl_product_id():
    product_list = []
    i = 1
    while (True):
        print("Crawl page: ", i)
        print(page_url.format(i))
        response = requests.get(page_url.format(i), headers=headers)
        
        if (response.status_code != 200):
            break

        products = json.loads(response.text)["data"]

        if (len(products) == 0):
            break

        for product in products:
            product_id = str(product["id"])
            print("Product ID: ", product_id)
            product_list.append(product_id)

        i += 1

    return product_list, i

def save_product_id(product_list=[]):
    with open(product_id_file, "w+", encoding='utf-8') as file:
        str = "\n".join(product_list)
        file.write(str)
    print("Save file: ", product_id_file)

# crawl product id
product_list, page = crawl_product_id()

print("No. Page: ", page)
print("No. Product ID: ", len(product_list))

# save product id for backup
save_product_id(product_list)
