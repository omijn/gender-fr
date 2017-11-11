import sys
import sqlite3

conn = sqlite3.connect('french_words.sqlite')
c = conn.cursor()

def noun_gender(noun):
	n = (noun,)
	c.execute("SELECT gender_id FROM word WHERE word=?", n)
	
	try:
		g = c.fetchone()[0]
		return g
	except Exception as e:
		return 4

if __name__ == '__main__':
	print(noun_gender(sys.argv[1]))