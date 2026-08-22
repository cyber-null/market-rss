from config.env_config import TZ
from datetime import datetime
from zoneinfo import ZoneInfo


def format_rss_description(data):
    timestamp = datetime.now(ZoneInfo(TZ)).strftime("%Y-%m-%d (%H:%M)")

    description = [f"""
    <h2>📊 Market Update</h2>

    {timestamp}
    """]

    for item in data:
        description.append(
            f"""
            <p>
                <strong>{item["symbol"].upper()}</strong><br>
                Price: {float(item["price"]):,}<br>
                Change: {item["change"]}%
            </p>
            --------------------------
            """
        )

    return "\n".join(description)
