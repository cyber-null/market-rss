import json

class Market_parser:
    def __init__(self) -> None:
        pass

    def parse_market(self, data):
        table = []

        for symbol, info in data["stats"].items():

            table.append({
                "symbol": symbol,
                "price": info["latest"],
                "chage": info["dayChange"]
            })

        return table

