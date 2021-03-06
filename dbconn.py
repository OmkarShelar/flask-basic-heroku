import os
from urllib import parse
import psycopg2

parse.uses_netloc.append("postgres")
url = parse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

def dbretrieve(id):
	cur = conn.cursor()
	cur.execute('SELECT value from test WHERE key='+str(id))
	rows = cur.fetchall()
	print(rows)
	for row in rows:
		return row[0]