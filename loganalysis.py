#!/usr/bin/env python3

import logsdb


def main():
    print_top_three()
    print_top_authors()
    print_error_days()
    return


def print_top_three():
    topThree = logsdb.get_top_three_articles()
    print("Top Three Articles:")
    print("---------------------------------------------------")
    for i in range(0, len(topThree)):
        print("{}  --  {} views".format(topThree[i][0], topThree[i][1]))
    print


def print_top_authors():
    topAuthors = logsdb.get_top_authors()
    print("Most Viewed Authors:")
    print("---------------------------------------------------")
    for i in range(0, len(topAuthors)):
        print("{}  --  {} views".format(topAuthors[i][0], topAuthors[i][1]))
    print


def print_error_days():
    errorDays = logsdb.get_days_with_most_errors()
    print("Days With > 1% Page View Errors:")
    print("---------------------------------------------------")
    for i in range(0, len(errorDays)):
        print("{}  --  {}% errors".format(errorDays[i][0], errorDays[i][1]))


if __name__ == '__main__':
    main()
