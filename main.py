import os
import sys

from listen_pending_treatment import start_listen

if __name__ == '__main__':
    try:
        start_listen()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
