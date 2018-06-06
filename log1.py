#!/usr/bin/env python
# PROJECT:-LOG ANALYSIS
import psycopg2
conn = psycopg2.connect(dbname="news")
cur = conn.cursor()


def popular_articles():
    print("THE POPULAR ARTICLES ARE:")
    cur.execute("select title,views from top_articles_views limit 3")
    result = cur.fetchall()
    i = 0
    while i < len(result):
        print (str(result[i]) + "views")
        i = i+1


def popular_authors():
    print("THE POPULAR AUTHORS ARE:")
    cur.execute("select * from top_authors_views ")
    result = cur.fetchall()
    i = 0
    while i < len(result):
        print (str(result[i]) + "views")
        i = i+1


def error_percentage():
    print("THE ERROR '%' IS:")
    cur.execute('''select to_char(day, 'Mon DD, YYYY') as day, percentage
                  from errors_percent where percentage > 1.0 group by day,
                  percentage order by percentage desc;''')
    result = cur.fetchall()
    for i in range(len(result)):
        date = result[i][0]
        errors_percent = result[i][1]
        print("%s--%.1f %%" % (date, errors_percent))
popular_articles()
popular_authors()
error_percentage()
cur.close()
conn.close()
