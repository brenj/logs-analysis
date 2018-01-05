"""SQL queries for logs-analysis."""

TOP3_ARTICLES = """
SELECT articles.title, count(*) AS views
FROM log, articles
WHERE log.path = '/article/' || articles.slug
GROUP BY articles.id
ORDER BY views DESC
LIMIT 3;
"""

TOP_AUTHORS = """
SELECT authors.name, sum(views_by_article) AS views_by_author
FROM (
    SELECT articles.author AS author, count(*) AS views_by_article
    FROM log, articles
    WHERE log.path = '/article/' || articles.slug
    GROUP BY articles.id
    ORDER BY views_by_article
    ) AS views_by_article_table, authors
WHERE author = authors.id
GROUP BY authors.id
ORDER BY views_by_author DESC;
"""

ERROR_PERCENTAGE = """
SELECT *
FROM (
    SELECT edb.day, (edb.errors * 100)::decimal / rbd.requests AS percentage
    FROM errors_by_day edb, requests_by_day rbd
    WHERE edb.day = rbd.day
    ) AS percentage_table
WHERE percentage > 1.0;
"""
