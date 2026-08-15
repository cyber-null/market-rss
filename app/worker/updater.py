from api.nobitex_api import Market_call
from parser.nobitex_parser import nobit_parse
from rendering.rss import gen_rss

import time

# setup logging
import logging
log = logging.getLogger(__name__)

current_rss = None

def update():
    global current_rss

    log.info("Call nobitex API")
    client = Market_call()
    data = client.get_market_price(
        [
            "btc",
            "usdt"
        ],
        # "usdt" # rls(default) or usdt
    )

    log.info("parse nobitex API data")
    data_parsed = nobit_parse(data)
    log.debug(f"Parsed Data: {data_parsed}")

    current_rss = gen_rss(data_parsed)
    log.debug(f"current_rss XML: {current_rss}")

    log.info("RSS Updated")


def get_current_rss():
    return current_rss


def run(interval=300):
    while True:
        try:
            update()

        except Exception as error:
            log.error(f"Update Failed: {error}")

        time.sleep(interval)
