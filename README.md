Project: Logs Analysis
======================

About
-----
From Udacity:
> You will analyze data from the logs of a web service to answer questions
such as "What is the most popular page?" and "When was the error rate high?"
using advanced SQL queries.

Supporting courses:
  * Intro to Relational Databases
  
Usage
-----
```console
usage: logs-analysis [options]

Tool for analyzing news data provided by Udacity

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             show answers to all analysis questions
  -ta, --top3-articles  show the three most popular articles of all time
  -tu, --top-authors    show the most popular authors of all time
  -et, --error-thresh   show the days where >1% of requests led to errors
```

Views
-----
Postgres views used for logs-analysis script.

```sql
CREATE VIEW requests_by_day AS
SELECT time::date AS day, count(*) AS requests
FROM log
GROUP BY day;
```

```sql
CREATE VIEW errors_by_day AS
SELECT time::date AS day, count(*) AS errors
FROM log
WHERE status = '404 NOT FOUND'
GROUP BY day;
```

Requirements
------------
* Vagrant or `postgres` and `psycopy2`
* The news database and news data are installed (see [Install Newsdata](https://github.com/brenj/logs-analysis#install-newsdata))

Install
-------
There are a number of ways to install `logs-analysis` depending on your
current setup. To install from scratch:

1. [Install the VM](https://github.com/brenj/logs-analysis#install-vm)
2. [Install the news data](https://github.com/brenj/logs-analysis#install-newsdata)
3. [Install logs-analysis](https://github.com/brenj/logs-analysis#install-logs-analysis)

Install VM
----------
1. `git clone https://github.com/udacity/fullstack-nanodegree-vm.git fullstack && cd fullstack/vagrant`
2. `vagrant up`
3. `vagrant ssh`

Install Newsdata
----------------
1. `wget https://github.com/brenj/logs-analysis/blob/master/newsdata.zip?raw=true -O newsdata.zip`
2. `unzip newsdata.zip`
3. `psql -d news -f newsdata.sql`

Note: `newsdata.zip` from `brenj/logs-analysis` contains the necessary views
to run `logs-analysis`. If you are using the original `newsdata.zip` data then
make sure to create the required views (see [Views](https://github.com/brenj/logs-analysis#views)).

Install logs-analysis
---------------------
1. `git clone https://github.com/brenj/logs-analysis.git && cd logs-analysis`
2. `./logs-analysis.py --all`

Code Quality
------------
This code base adheres to the [PEP8](https://www.python.org/dev/peps/pep-0008/) standard.

Grading (by Udacity)
--------------------

Criteria       |Highest Grade Possible  |Grade Recieved
---------------|------------------------|-------------------
Functionality  |Meets Specifications    |TDB
Code Quality   |Meets Specifications    |TDB
README File    |Meets Specifications    |TDB
