import requests

def get_market_price(src, dst="rls"):
    url = "https://apiv2.nobitex.ir/market/stats"
    params = {
        "srcCurrency": src,
        "dstCurrency": dst
    }
    headers = {
        'Accept': 'application/json',
        # 'User-Agent': 'TraderBot/MyBot-1.0.0'
    }

    try:
        # session = requests.session()
        respons = requests.get(
            url,
            headers=headers,
            params=params
        )
        respons.raise_for_status()

        data = respons.json()
        price = data["stats"][f"{src}-{dst}"]["latest"]

        return price

    except Exception as error:
        return error


if __name__ == "__main__":
    market = get_market_price("usdt")
    print(market)
