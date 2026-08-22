from config.env_config import TZ
from feedgen.feed import FeedGenerator
from rendering.format import format_rss_description

from datetime import datetime
from zoneinfo import ZoneInfo
import uuid
import logging

log = logging.getLogger(__name__)


def gen_rss(data):
    fg = FeedGenerator()
    
    fg.title("Market Price")
    fg.description("this must return Market Price")
    fg.link(
        href="http://localhost:5000/rss",
        rel="self"
    )

    log.info("Create entry")

    entry = fg.add_entry()

    entry.id(str(uuid.uuid4()))

    entry.title(f"Market Price: {datetime.now(ZoneInfo(TZ))}")

    log.info("Create description")
    description = format_rss_description(data)

    log.debug(f"description has been created: {description}")
    entry.description(description)

    entry.pubDate(datetime.now(ZoneInfo(TZ)))


    return fg.rss_str(
        extensions=True,
        pretty=True
    )
