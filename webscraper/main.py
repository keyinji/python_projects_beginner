from bs4 import BeautifulSoup
import requests

# retrieve the web page and parse the contents
try:
    mainpage = requests.get('https://coinmarketcap.com/currencies/binance-coin/')
    mainpage.raise_for_status()  # Raises a HTTPError if the HTTP request returned an unsuccessful status code
    soup = BeautifulSoup(mainpage.content, 'html.parser')
    
    ok = soup.find_all("div", {"class":"readmoreDesc"})

    # Check if the desired div is found
    if ok:
        title = ok[0].find_all("h3")

        # Check if the title is found
        if title:
            print(title[0].text.strip() + "\n")
        else:
            print("Title not found.")

        for p in ok[0].find_all('p'):
            print(p.text.strip() + "\n")

    else:
        print("Specified class not found in the webpage.")

except requests.exceptions.RequestException as e:
    print("Error during requests to CoinMarketCap:", str(e))
