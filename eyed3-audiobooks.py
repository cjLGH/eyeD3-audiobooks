#! /usr/bin/env python
import readline
import eyed3

artist = ''
while not artist:
  artist = raw_input("artist: ")
  artist = str(artist)
  artist = unicode(artist, "utf-8")

album = ''
while not album:
  album = raw_input("album: ")
  album = str(album)
  album = unicode(album, "utf-8")

album_artist = ''
while not album_artist:
  album_artist = raw_input("album_artist: ")
  album_artist = str(album_artist)
  album_artist = unicode(album_artist, "utf-8")

title = ''
while not title:
  title = raw_input("Title: ")
  title = str(title)
  title = unicode(title, "utf-8")

genre = ''
while not genre:
  genre = raw_input("genre: ")
genre = int(genre)

audiofile = eyed3.load("1.mp3")
audiofile.tag.title         = title
audiofile.tag.album         = album
audiofile.tag.album_artist  = album_artist
audiofile.tag.title         = title
audiofile.tag.genre         = genre
audiofile.tag.save()
