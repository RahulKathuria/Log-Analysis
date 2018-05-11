## Why this project?

In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

## Report generation
Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.

## How to run:
 
 1. First of all you have to download and install vagrant and virtual box.
 2. Download the data from this [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
 3. Now this is the main database in the downloaded file. 
 4. Clone this repo and move newsdata.sql into the downloaded folder.
 5. Now open terminal and write these commands to run virtual machine:
    	
		a) vagrant up
    	b) vagrant ssh
    	c) cd /vagrant
    	d) psql -d news -f newsdata.sql
    	e) pswl -d news
6. These commands will load the database and connect you to it too.
7. Now after running all these commands, simply run "python newsdata.py" on your terminal.
