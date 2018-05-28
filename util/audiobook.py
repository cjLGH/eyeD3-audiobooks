import readline
import sys

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
