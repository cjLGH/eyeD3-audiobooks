#! /usr/bin/env python
import readline
import eyed3

title = ''
while not title:
  title = raw_input("Title: ")
  title = str(title)
  title = unicode(title, "utf-8")

print(title)

genre = raw_input("Genre: ")
genre = int(genre)
# genre = unicode(genre, "utf-8")

audiofile = eyed3.load("1.mp3")
audiofile.tag.title = title
audiofile.tag.genre = genre
audiofile.tag.save()
