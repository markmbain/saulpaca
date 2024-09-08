import csv
import requests
from bs4 import BeautifulSoup
import time
import re

csv.register_dialect('custom', delimiter=',', quoting=csv.QUOTE_NONE, escapechar=' ')

def scrape_attorney_info(number):
    url = f"https://apps.calbar.ca.gov/attorney/Licensee/Detail/{number}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    name_element = soup.find('b', string=re.compile('#'))
    if name_element:
        full_text = name_element.text.strip()
        name_parts = full_text.split('#')
        name = ' '.join(name_parts[0].split())  # Remove extra spaces
        attorney_number = name_parts[1].strip() if len(name_parts) > 1 else "N/A"
    else:
        name = "N/A"
        attorney_number = "N/A"
    
    # Extract address
    address_element = soup.find('p', string=re.compile('Address:'))
    if address_element:
        address = address_element.text.strip().replace('Address:', '').strip()
    else:
        address = "N/A"
    
    # Extract phone number
    phone_element = soup.find('p', string=re.compile('Phone:'))
    if phone_element:
        phone_text = phone_element.text.strip()
        phone_match = re.search(r'Phone:\s*([\d-]+)', phone_text)
        phone = phone_match.group(1) if phone_match else "N/A"
    else:
        phone = "N/A"
    
    return {
        'Name': name,
        'Number': attorney_number,
        'Address': address,
        'Phone': phone
    }

def main(num_attorneys_to_scrape):
    with open('cal_bar_palo_alto_attorneys.csv', 'r') as file:
        reader = csv.DictReader(file)
        attorneys = list(reader)

    numbers = [attorney['Number'] for attorney in attorneys][:num_attorneys_to_scrape]

    attorneys_info = []
    for number in numbers:
        info = scrape_attorney_info(number)
        attorneys_info.append(info)
        time.sleep(1)
        print(f"Scraped info for attorney number {number}: {info['Name']} ({info['Number']})")

    # Remove backslashes from addresses
    for attorney in attorneys_info:
        attorney['Address'] = attorney['Address'].replace('\\', '')

    with open('cal_bar_attorneys_info.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Number', 'Address', 'Phone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for attorney in attorneys_info:
            # Remove extra spaces from all fields
            cleaned_attorney = {k: ' '.join(v.split()) if isinstance(v, str) else v 
                                for k, v in attorney.items()}
            writer.writerow(cleaned_attorney)

    print(f"Scraping completed. Data for {len(attorneys_info)} attorneys saved to cal_bar_attorneys_info.csv")

if __name__ == "__main__":
    num_attorneys = int(input("Enter the number of attorneys to scrape: "))
    main(num_attorneys)
