
import psycopg2


def get_top_three_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT title, COUNT(*) AS views " +
              "FROM articles, log " +
              "WHERE path != '/' AND path LIKE CONCAT('%/', slug) " +
              "GROUP BY title " +
              "ORDER BY views DESC " +
              "LIMIT 3;")
    articles = c.fetchall()
    db.close()
    return articles


def get_top_authors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT authors.name AS author, COUNT(*) AS views " +
              "FROM log, articles, authors " +
              "WHERE log.path != '/'" +
              "AND log.path LIKE CONCAT('%/', articles.slug) " +
              "AND articles.author = authors.id " +
              "GROUP BY authors.name " +
              "ORDER BY views DESC;")
    authors = c.fetchall()
    db.close()
    return authors


def get_days_with_most_errors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT err.date AS date," +
              "ROUND(((err.num * 1.0 / (err.num + ok.num)) * 100), 2) AS per" +
              " FROM err, ok " +
              "WHERE err.date = ok.date " +
              "AND ((err.num * 1.0 / (err.num + ok.num)) * 100) > 1 " +
              "ORDER BY date;")
    days = c.fetchall()
    db.close()
    return days
