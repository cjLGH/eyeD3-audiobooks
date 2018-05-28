#!/bin/sh
''''which python    >/dev/null 2>&1 && exec python    "$0" "$@" # '''
''''which python2   >/dev/null 2>&1 && exec python2   "$0" "$@" # '''
''''which python2.7 >/dev/null 2>&1 && exec python2.7 "$0" "$@" # '''
''''exec echo "Error: Python not found!" # '''

import eyed3
import readline
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

def shutdown():
    sys.exit(0)

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

def get_artist():
    while True:
        artist = raw_input("artist: ")
        if artist:
          break
        else:
          continue
    return unicode(artist, "utf-8")

def get_album():
    while True:
        album = raw_input("album: ")
        if album:
          break
        else:
          continue
    return unicode(album, "utf-8")

def get_album_artist():
    while True:
        album_artist = raw_input("album_artist: ")
        if album_artist:
          break
        else:
          continue
    return unicode(album_artist, "utf-8")

def get_title():
    while True:
        title = raw_input("title: ")
        if title:
          break
        else:
          continue
    return unicode(title, "utf-8")

def get_genre():
    while True:
        try:
            genre = int(raw_input("genre: "))
        except ValueError:
            continue
        else:
            break
    return genre

def main():
    if not which("eyeD3"):
        print('!!! eyeD3 required !!!')
        print('Install eyeD3: pip install eyeD3')
        shutdown()

    for i in os.listdir('.'):
      if i.endswith('.mp3'):
        print(i)

        artist = get_artist()
        album = get_album()
        album_artist = get_album_artist()
        title = get_title()
        genre = get_genre()

        audiofile = eyed3.load(i)
        audiofile.tag.artist        = artist
        audiofile.tag.album         = album
        audiofile.tag.album_artist  = album_artist
        audiofile.tag.title         = title
        audiofile.tag.genre         = genre
        audiofile.tag.save()

# Call main()
if __name__ == "__main__":
    main()
