import json

def parse_market(data):
    table = []

    for symbol, info in data["stats"].items():

        table.append({
            "symbol": symbol,
            # "price": f"{(int(info["latest"])//10):,}", # for change rial to toman
            "price": info["latest"],
            "change": info["dayChange"]
        })

    return table
