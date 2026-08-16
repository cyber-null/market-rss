from feedgen.feed import FeedGenerator
from config import TZ

from datetime import datetime
from zoneinfo import ZoneInfo
import uuid


def gen_rss(data):
    fg = FeedGenerator()
    
    fg.title("Market Price")
    fg.description("this must return Market Price")
    fg.link(
        href="http://localhost:5000/rss",
        rel="self"
    )

    for item in data:
        entry = fg.add_entry()

        entry.id(str(uuid.uuid4()))

        entry.title(f"Price: {item['symbol']}")

        entry.description(
            f"| Price: {float(item['price']):,} |\n"
            f"| Change%: {item['change']} |"
        )

        entry.pubDate(datetime.now(ZoneInfo(TZ)))


    return fg.rss_str(
        extensions=True,
        pretty=True
    )
