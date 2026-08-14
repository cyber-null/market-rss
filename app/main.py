# setup and initinals logging
from log_config import setup_logging
setup_logging()

from server.flask_server import server_start, app
from worker.updater import run, current_rss

import threading

import logging
log = logging.getLogger(__name__)

def main():
    updater_thread = threading.Thread(
        target=run,
        args=(300,),
        daemon=True
    )

    updater_thread.start()

    app.run(
        host="0.0.0.0",
        port=5000
    )



if __name__ == "__main__":
    log.info("start Program")
    main()
