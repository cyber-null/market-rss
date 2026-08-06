from tabulate import tabulate

def print_table(data):
    rows = []

    for item in data:
        rows.append([
            item["symbol"],
            item["price"],
            item["change"]
        ])

    print(
        tabulate(
            rows,
            headers=[
                "symbol",
                "price",
                "change"
            ],
            tablefmt="rounded_grid"
        )
    )
