from flask import Flask, Response
from worker.updater import get_current_rss

app = Flask(__name__)

@app.route("/rss")
def server_start():
    data = get_current_rss()

    print(f"DATA: {data}")
    print(f"type: {type(data)}")

    if data is None:
        return "RSS is not ready yet", 503

    return Response(
        data,
        mimetype="application/rss+xml"
    )
