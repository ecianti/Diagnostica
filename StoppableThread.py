

import threading
import time
import datetime
from utility import gfib, file_local_path


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, n):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()
        self.n = n

    def stop(self):
        print("Terminazione del thread")
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        pass


class LoggerThread(StoppableThread):
    def write_log(self):  # definisce funzione del log dei dati
        # with open(file_local_path, "a") as f:
        #     for i in range(5):
        #         time.sleep(2)
        #         i += 1
        #         now = datetime.datetime.now()
        #         log_string = "{}{}{}\n".format(str(now.isoformat()), " "*10, gfib)
        #         f.write(log_string)
        #         print(log_string)
        #         f.close()
        for i in range(5):
            if not self.stopped():
                now = datetime.datetime.now()
                log_string = "{:4} {}{}{}".format(self.n, str(now.isoformat()), " " * 10, gfib)
                print(log_string)
                time.sleep(1)
            else:
                return

    def run(self):
        self.write_log()