#!/usr/bin/env python3

from logsdb import send_query


def main():
    print_top_three()
    print_top_authors()
    print_error_days()
    return


def print_top_three():
    topThree = send_query("""
              SELECT title, COUNT(*) AS views
              FROM articles, log
              WHERE path LIKE CONCAT('/article/', slug)
              GROUP BY title
              ORDER BY views DESC
              LIMIT 3;
              """)
    print("Top Three Articles:")
    print("---------------------------------------------------")
    for i in range(0, len(topThree)):
        print("{}  --  {} views".format(topThree[i][0], topThree[i][1]))
    print


def print_top_authors():
    topAuthors = send_query("""
              SELECT authors.name AS author, COUNT(*) AS views
              FROM log, articles, authors
              WHERE log.path LIKE CONCAT('/article/', articles.slug)
              AND articles.author = authors.id
              GROUP BY authors.name
              ORDER BY views DESC;
              """)
    print("Most Viewed Authors:")
    print("---------------------------------------------------")
    for i in range(0, len(topAuthors)):
        print("{}  --  {} views".format(topAuthors[i][0], topAuthors[i][1]))
    print


def print_error_days():
    errorDays = send_query("""
              SELECT err.date AS date,
              ROUND(((err.num * 1.0 / (err.num + ok.num)) * 100), 2) AS per
              FROM err, ok
              WHERE err.date = ok.date
              AND ((err.num * 1.0 / (err.num + ok.num)) * 100) > 1
              ORDER BY date;
              """)
    print("Days With > 1% Page View Errors:")
    print("---------------------------------------------------")
    for i in range(0, len(errorDays)):
        print("{}  --  {}% errors".format(errorDays[i][0], errorDays[i][1]))


if __name__ == '__main__':
    main()
