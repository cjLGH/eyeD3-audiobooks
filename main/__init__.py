import signal
import sys

def sig_handler(signum=None, frame=None):
    if signum is not None:
        print('Signal %d caught, saving and exiting...' % signum)
        shutdown()

# Register signals, such as CTRL + C
signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

def shutdown():
    sys.exit(0)
