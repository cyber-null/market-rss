def nobit_parse(data):
    table = []

    for symbol, info in data["stats"].items():
        table.append({
            "symbol": symbol,
            "price": info["latest"],
            "change": info["dayChange"]
        })

    return table
