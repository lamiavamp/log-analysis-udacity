#!/usr/bin/env python3

import psycopg2
import datetime


def connect(database_name):
    """
     Connect to the PostgreSQL database.
     Return a database connection.
     """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.Error as err:
        print ("Unable to connect to the database")
        print(err)
        sys.exit(1)


# intializing database connection
DBNAME = "news"
db, c = connect(DBNAME)


# What are the most popular three articles of all time?
def top_articles():
    c.execute("""select title, count(path) as top
    from articles, log
    where path = concat('/article/',slug)
    and status='200 OK'
    group by title
    order by top desc
    limit 3;""")
    result = c.fetchall()

    # printing results
    print ("Top articles:")
    for row in result:
        print ("\""+row[0]+"\" -- ", row[1], "views")


# Who are the most popular article authors of all time?
def pop_auths():
    c.execute("""select name, count(path) as top
    from articles, log, authors
    where path = concat('/article/',slug)
    and status='200 OK'
    and authors.id = articles.author
    group by name
    order by top desc
    limit 4;""")
    result = c.fetchall()

    # printing results
    print ("Most popular authors:")
    for row in result:
        print ("\""+row[0]+"\" -- ", row[1], "views")


# On which days did more than 1% of requests lead to errors?
def error_rate():
    c.execute("""select * from
    (select t_requests.day,
    round((t_errors.errors*100)/cast(t_requests.requests as numeric),2)
    as err_rate
    from
    (select date(time) as day,
    sum(case when status != '200 OK' then 1 else 0 end) as errors
    from log group by day) as t_errors
    inner join
    (select date(time) as day,
    count(status) as requests from log group by day) as t_requests
    on
    t_errors.day = t_requests.day) as final_q
    where err_rate > 1.0;""")
    result = c.fetchall()

    # printing results
    print ("Days with more than 1% error rate encountered:")
    for row in result:
        print ("%s -- %.2f%%" % (row[0].strftime("%b %d, %Y"), row[1]))


if __name__ == '__main__':
    top_articles()
    print()
    pop_auths()
    print()
    error_rate()
    db.close()
