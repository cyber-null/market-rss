# setup and initinals logging
from log_config import setup_logging
setup_logging()

from config import UPDATE_INTERVAL, APP_HOST, APP_PORT
from server.flask_server import server_start, app
from worker.updater import run, current_rss

import threading

import logging
log = logging.getLogger(__name__)


def main():
    updater_thread = threading.Thread(
        target=run,
        args=(UPDATE_INTERVAL,),
        daemon=True
    )

    updater_thread.start()

    app.run(
        host=APP_HOST,
        port=APP_PORT
    )



if __name__ == "__main__":
    log.info("------ # START PROGRAM # -----")
    main()
