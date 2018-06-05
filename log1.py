#! /usr/bin/env
#PROJECT:-LOG ANALYSIS
import psycopg2
conn = psycopg2.connect(dbname="news")
cur = conn.cursor()
print("create successfully")
try:
    q1 = '''create view top_articles_views as select title, author,
            count(title) as views from articles, log
            where log.path like concat('%', articles.slug)
            group by articles.title, articles.author
            order by views desc;
         '''
    print("view created")
except:
    print("unsuccessful")


def popular_articles():
    print("THE POPULAR ARTICLES ARE:")
    cur.execute("select title,views from top_articles_views limit 3")
    result = cur.fetchall()
    i = 0
    while i < len(result):
        print (str(result[i]) + "views")
        i = i+1


try:
    q2 = '''create view top_authors_views as select name,
            count(articles.author) as views from articles, authors, log
            where log.path like concat('%', articles.slug) and
            articles.author=authors.id group by authors.name
            order by views desc;
         '''
    print("view created")
except:
    print("unsuccessful")


def popular_authors():
    print("THE POPULAR AUTHORS ARE:")
    cur.execute("select * from top_authors_views ")
    result = cur.fetchall()
    i = 0
    while i < len(result):
        print (str(result[i]) + "views")
        i = i+1


try:
    q3 = '''create view total_requests as select count(*) as total,
            date(time) as day from log group by day order by day desc;
         '''
    q4 = '''create view error_requests as select count(*) as total,
            date(time) as day from log where status != '200 OK'
            group by day order by total desc;
         '''
    q5 = '''create view errors_percent as select total_requests.day,
            round((100.0*error_requests.total)/total_requests.total,2)
            as percentage from error_requests, total_requests
            where error_requests.day=total_requests.day;
         '''
    print("view created")
except:
    print("unsuccessful")


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
