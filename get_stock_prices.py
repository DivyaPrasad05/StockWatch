import requests
from bs4 import BeautifulSoup


def get_stock_data(stock_symbol: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    url = f"https://ca.finance.yahoo.com/quote/{stock_symbol}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Finds the price of the stock using just its symbol
    price = float(
        soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all("fin-streamer")[0].text
    )  # works for both upper, lower, and mixed case

    # Finds the price difference from the previous close:
    change_pts = (
        soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all("fin-streamer")[1].text
    )
    change_percent = (
        soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all("fin-streamer")[2].text
    )
    return price, change_pts, change_percent
