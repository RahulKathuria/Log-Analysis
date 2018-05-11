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

query1_solution = ("""select articles.title as title, count(*) as total 
                      from articles, log where log.path = '/article/' || articles.slug 
                      group by articles.title order by total desc limit 3;""")
query2_solution = ("""select authors.name , count(*) as total from authors, 
            articles, log where articles.author = authors.id and 
            articles.slug  = substr(log.path,10) group by authors.name 
            order by total desc""")
query3_solution = (""" """)

print_query(query2,query2_solution)
			