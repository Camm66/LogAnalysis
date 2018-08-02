
import psycopg2


def send_query(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result
