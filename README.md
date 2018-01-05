Logs Analysis
=============

About
-----
From Udacity:
> You will analyze data from the logs of a web service to answer questions
such as "What is the most popular page?" and "When was the error rate high?"
using advanced SQL queries.

Supporting courses:
  * Intro to Relational Databases
  
Requirements
------------
* Vagrant

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

Install
-------
1. `git clone https://github.com/udacity/fullstack-nanodegree-vm.git fullstack && cd fullstack/vagrant`
2. `vagrant up`
3. `vagrant ssh`

Code Quality
------------
This code base adheres to [PEP8](https://www.python.org/dev/peps/pep-0008/)

Grading (by Udacity)
--------------------

Criteria       |Highest Grade Possible  |Grade Recieved
---------------|------------------------|-------------------
Functionality  |Meets Specifications    |Meets Specifications
Code Quality   |Meets Specifications    |Meets Specifications
README File    |Meets Specifications    |Meets Specifications
