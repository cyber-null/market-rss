from api import Market_call
from parser import parse_market
from table import print_table 


def main():
    client = Market_call()

    data = client.get_market_price(
        [
            "btc",
            "usdt",
            "eth"
        ],
        # "usdt" # rls(default) or usdt
    )

    # parse data
    parsed = parse_market(data=data)

    # create table
    print_table(parsed)


if __name__ == "__main__":
    main()
