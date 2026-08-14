from feedgen.feed import FeedGenerator
from datetime import datetime, timezone


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

        entry.title(f"Price: {item['symbol']}")

        entry.description(
            f"| Price: {item['price']} |"
            f"| Change%: {item['change']} |"
        )

        entry.pubDate(datetime.now(timezone.utc))


    return fg.rss_str(
        extensions=True,
        pretty=True
    )
