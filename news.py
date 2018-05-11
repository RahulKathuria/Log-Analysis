#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2

DBNAME = 'news'


def newsData_query(query):
    """This function helps to connect to the database and return the solution of the query"""

    db = psycopg2.connect(database=DBNAME)
    news_cursor = db.cursor()
    news_cursor.execute(query)
    query_answer = news_cursor.fetchall()
    db.close()
    return query_answer


def print_query(query_ques, query_ans):
    print (query_ques)
    result = newsData_query(query_ans)
    print(result) 


query1 = ["""What are the most popular articles of all time?"""]
query2 = ["""Who are the most popular article authors of all time?"""]
query3 = \
    ["""On which days did more than 1% of requests lead to errors?"""]

query1_solution = ("""
            SELECT 
                articles.title as title,
                count(*) as total 
            FROM 
                articles, log 
            WHERE 
                log.path = '/article/' || articles.slug 
            GROUP BY 
                articles.title 
            ORDER BY 
                total desc limit 3;""")
query2_solution = ("""
            SELECT 
                authors.name,
                count(*) as total
            FROM 
                authors, 
                articles,
                log 
            WHERE
                articles.author = authors.id
            AND 
                articles.slug  = substr(log.path,10)
            GROUP BY 
                authors.name 
            ORDER BY total desc""")
query3_solution = ("""
        SELECT 
            *
        FROM 
            (SELECT  
                err.date,
                round(100 * err.e / requests.r,2) as p
            FROM
                (SELECT 
                    date(time) as date, 
                    count(status) as e
                FROM 
                    log
                WHERE 
                    status != '200 OK'
                GROUP BY
                    date 
                ORDER BY
                    date) err,
                (SELECT
                    date(time) as date, 
                    count(status) as r
                FROM 
                    log
                GROUP BY
                    date
                ) requests
            WHERE
                err.date = requests.date) analysis

        WHERE 
            p > 1.00
            """)
print_query(query1,query1_solution)
print_query(query2,query2_solution)
print_query(query3,query3_solution)
            