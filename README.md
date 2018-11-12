# Log Analysis
This project is created in regards to have a simple API to deal with a news database

## Content
- **news-db-api.py:** postgress API to the database
- **log-output.txt:** sample output
- **db-tables:** a description of the tables in the database

## Dependencies
You need to install python `psycopg2` module
`pip3 install psycopg2`

## Installation
`$ git clone https://github.com/lamiavamp/log-analysis-udacity.git`
`$ cd log-analysis-udacity`

## Usage
Simply run the following script
`python3 news-db-api.py`

Running the code produces *three* outputs answering these questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Enjoy!
