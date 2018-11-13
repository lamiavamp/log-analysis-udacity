# Log Analysis
This project sets up an API dealing with a PostgreSQL news database that consists of a huge collection of articles. The main purpose of the project is to retrive meaningful information from the database.

The provided `news-db-api.py` script query the database to answer the folwwoing questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting Started

## Content
- **news-db-api.py:** postgress API to the database
- **log-output.txt:** sample output
- **db-tables:** a description of the tables in the database

### Prerequissites
- The code is running on python3, make sure it is installed. To install `python3` in Mac use homebrew: 
`$ brew install python3`
or follow [this link](https://realpython.com/installing-python) for other OS 
- You need to install python `psycopg2` module:
`pip3 install psycopg2`

### Installation
* clone the repository using git
`$ git clone https://github.com/lamiavamp/log-analysis-udacity.git`
`$ cd log-analysis-udacity`

* download the databse using [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* unzip the file and run the following command to import it into the database
`$ psql -d news -f newsdata.sql`

### Usage
Simply run the following script to get the results
`python3 news-db-api.py`

## Author
* **Lamia** - [lamiavamp](https://github.com/lamiavamp)
