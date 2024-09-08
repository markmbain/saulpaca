import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

from multion.client import MultiOn

MULTION_API_KEY = os.getenv("MULTION_API_KEY")

client = MultiOn(api_key=MULTION_API_KEY)


# Example of using the multion client to browse a website, in this case, Amazon website.
def multion_browse(url, product_name):
    browse_response = client.browse(
        cmd=f"What is the price of {product_name}.",
        url=url,
    )
    browse_response_result = browse_response.message
    print(browse_response_result)
    return browse_response_result


# Example of using the multion client to retrieve data from a website, in this case, H&M website.
def multion_retrieve_response(url):
    retrieve_response = client.retrieve(
        url=url,
        cmd="Get all items and their name, price, colors, purchase url, and image url.",
        fields=["name", "price", "colors", "purchase_url", "image_url"],
        render_js=True,
        scroll_to_bottom=True,
        max_items=2,
    )
    data = retrieve_response.data
    print(data)
    return data


if __name__ == "__main__":
    retrieve_response_url = "https://www2.hm.com/en_us/men/products/view-all.html"
    multion_retrieve_response(retrieve_response_url)

    # retrieve_response_sample_response = """
    # [
    # {'name': 'Regular Fit Hoodie', 'price': '34.99', 'colors': 'Black, Light beige, Cream', 'purchase_url': 'https://www2.hm.com/en_us/productpage.1103620001.html', 'image_url': 'https://image.hm.com/assets/hm/22/41/224187bcaa0dcd67dc3beb7014467156b9af25c7.jpg?imwidth=256'},
    # {'name': 'Loose Jeans', 'price': '39.99', 'colors': 'Light denim blue, Denim black, Light denim blue, Dark blue', 'purchase_url': 'https://www2.hm.com/en_us/productpage.1130274013.html', 'image_url': 'https://image.hm.com/assets/hm/d9/f4/d9f444c3f835bd735010e318b468d71921864bda.jpg?imwidth=256'}
    # ]
    # """

    multion_browser_url = "https://www.google.com/"
    product_name = "Iphone 15 pro max"
    multion_browse(multion_browser_url, product_name)

    # multion_browser_sample_response = """
    # The price of the iPhone 15 Pro Max varies based on the storage capacity and the retailer. Here are some prices I found:

    # 1. iPhone 15 Pro Max 256GB Natural Titanium Unlocked - $1,199.00 from Apple.
    # 2. iPhone 15 Pro Max 1TB Blue Titanium Unlocked - $1,599.00 from Apple.
    # 3. Restored Apple iPhone 15 Pro - Carrier Unlocked - 256 GB Natural Titanium (Refurbished) - $914.45 from Walmart.
    # """
