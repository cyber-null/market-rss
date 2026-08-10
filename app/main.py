# setup and initinals logging
from logger import setup_logging
setup_logging()

import logging
from api.nobitex_api import Market_call
from parser.nobitex_parser import nobit_parse

import time

log = logging.getLogger(__name__)

def main():
    client = Market_call()

    # log.info("get market price from nobitex API")
    data = client.get_market_price(
        [
            "btc",
            "usdt"
        ],
        # "usdt" # rls(default) or usdt
    )

    # log.info("parse nobitex API data")
    data_parsed = nobit_parse(data)

    print(data_parsed)



if __name__ == "__main__":
    log.info("start Program")
    main()
    # while True:
    #     try:
    #         main()

    #     except Exception as error:
    #         raise RuntimeError(
    #             f"Error: {error}"
    #         )

    log.info("sleep time!!")
    #     time.sleep(60)
