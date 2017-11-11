import sys
import sqlite3

conn = sqlite3.connect('french_words.sqlite')
c = conn.cursor()

def noun_gender(noun):
	n = (noun,)
	c.execute("SELECT gender_id FROM word WHERE word=?", n)
	return c.fetchone()[0]
