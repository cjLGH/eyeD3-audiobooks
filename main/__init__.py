import os
import signal
import sys

def sig_handler(signum=None, frame=None):
    if signum is not None:
        print('Signal %d caught, saving and exiting...' % signum)
        shutdown()

# Register signals, such as CTRL + C
signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)

def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def shutdown():
    sys.exit(0)
