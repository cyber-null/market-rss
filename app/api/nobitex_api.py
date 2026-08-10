import requests
import logging

log = logging.getLogger(__name__)

## use nobitex api

class Market_call:
    BASE_URL = "https://apiv2.nobitex.ir"

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({
            'Accept': 'application/json',
            'User-Agent': 'TraderBot/MyBot-1.0.0'
        })


    def get_market_price(self, currnncies, dst="rls"):

        url = f"{self.BASE_URL}/market/stats"

        params = {
            "srcCurrency": ",".join(currnncies),
            "dstCurrency": dst
        }

        try:
            log.info("GET post API")
            respons = self.session.get(
                url,
                params=params
            )

            respons.raise_for_status()

            return respons.json()

        except requests.RequestException as error:
             raise RuntimeError(
                f"Nobitex API error: {error}"
            )
