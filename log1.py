#!/usr/bin/env python
# PROJECT:-LOG ANALYSIS
import psycopg2
conn = psycopg2.connect(dbname="news")
cur = conn.cursor()


def popular_articles():
    print("THE POPULAR ARTICLES ARE:")
    cur.execute("select title,views from top_articles_views limit 3")
    result = cur.fetchall()
    for y in result:
        print '"', y[0], '"', '-- ', y[1], " views"


def popular_authors():
    print("THE POPULAR AUTHORS ARE:")
    cur.execute("select * from top_authors_views ")
    result = cur.fetchall()
    for z in result:
        print z[0], ' -- ', z[1], " views"


def error_percentage():
    print("THE ERROR '%' IS:")
    cur.execute(''' select to_char(day, 'Mon DD, YYYY') as day, percentage
                   from errors_percent where percentage > 1.0 group by day,
                   percentage order by percentage
                   desc;
                ''')
    result = cur.fetchall()
    for date, errors_percent in result:
        print('{} -- {:.1f}% errors'.format(date, errors_percent))
popular_articles()
popular_authors()
error_percentage()
cur.close()
conn.close()
