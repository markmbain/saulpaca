import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_attorneys(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    attorneys = []
    rows = soup.find_all('tr', class_='rowASRLodd')
    
    for row in rows:
        columns = row.find_all('td')
        if len(columns) == 5:
            name = columns[0].text.strip()
            status = columns[1].text.strip()
            number = columns[2].text.strip()
            city = columns[3].text.strip()
            admission_date = columns[4].text.strip()
            
            attorney = {
                'Name': name,
                'Status': status,
                'Number': number,
                'City': city,
                'Admission Date': admission_date
            }
            attorneys.append(attorney)
    
    print(f"Found {len(attorneys)} attorneys")
    return attorneys

def save_to_csv(attorneys, filename):
    if not attorneys:
        print("No attorneys found to save.")
        return

    keys = attorneys[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(attorneys)

def main():
    base_url = "https://apps.calbar.ca.gov/attorney/LicenseeSearch/AdvancedSearch"
    params = {
        'LastNameOption': 'b',
        'LastName': '',
        'FirstNameOption': 'b',
        'FirstName': '',
        'MiddleNameOption': 'b',
        'MiddleName': '',
        'FirmNameOption': 'b',
        'FirmName': '',
        'CityOption': 'b',
        'City': 'Palo alto',
        'State': '',
        'Zip': '',
        'District': '',
        'County': '',
        'LegalSpecialty': '',
        'LanguageSpoken': '',
        'PracticeArea': ''
    }
    
    url = "https://apps.calbar.ca.gov/attorney/LicenseeSearch/AdvancedSearch?LastNameOption=b&LastName=&FirstNameOption=b&FirstName=&MiddleNameOption=b&MiddleName=&FirmNameOption=b&FirmName=&CityOption=b&City=Palo+alto&State=&Zip=&District=&County=&LegalSpecialty=&LanguageSpoken=&PracticeArea="
    
    attorneys = scrape_attorneys(url)
    if attorneys:
        save_to_csv(attorneys, 'cal_bar_palo_alto_attorneys.csv')
        print(f"Scraped {len(attorneys)} attorneys and saved to cal_bar_palo_alto_attorneys.csv")
    else:
        print("No attorneys found. Check the search parameters or website structure.")

if __name__ == "__main__":
    main()
