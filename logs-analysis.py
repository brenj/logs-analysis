#!/usr/bin/env python
# encoding: utf-8

"""Tool for analyzing news data provided by Udacity."""

import argparse
import psycopg2
import sys

import queries

DATABASE_NAME = 'news'


def run_query(query):
    """Run a query against a database.

    Args:
        query (str): Query to run against database.

    Returns:
        list: Results from query.
    """
    with psycopg2.connect(dbname=DATABASE_NAME) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    return []


def print_top3_articles():
    """Print the top three news articles of all time."""
    print "The most popular articles of all time are:\n"
    for article, views in run_query(queries.TOP3_ARTICLES):
        print ' ' * 3,
        print '"{0}" with {1:,} views'.format(article, views)


def print_top_authors():
    """Print the top three authors of all time."""
    print "The most popular authors of all time are:\n"
    for author, views in run_query(queries.TOP_AUTHORS):
        print ' ' * 3,
        print '{0} with {1:,} views'.format(author, views)


def print_days_over_error_threshold():
    """Print which days had more than 1% of requests lead to errors."""
    print "The following days had more than 1% of requests lead to errors:\n"
    for day, error_percentage in run_query(queries.ERROR_PERCENTAGE):
        print ' ' * 3,
        print '{0}: {1:.2f}% of all requests resulted in an error'.format(
            day.strftime('%B %d, %Y'), error_percentage)


def main(args):
    """Main entry point for logs-analysis.

    Args:
        args (Namespace): Parsed command line options.

    Returns:
        int: An exit code; 0 (success) | >0 (failure).
    """
    if args.top3_articles:
        print_top3_articles()
    elif args.top_authors:
        print_top_authors()
    elif args.error_thresh:
        print_days_over_error_threshold()
    elif args.all:
        print_top3_articles()
        print
        print_top_authors()
        print
        print_days_over_error_threshold()
    else:
        return 1

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Tool for analyzing news data provided by Udacity',
        usage='logs-analysis [options]')

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-a", "--all", action="store_true",
        help="show answers to all analysis questions")

    group.add_argument(
        "-ta", "--top3-articles", action="store_true",
        help="show the three most popular articles of all time")

    group.add_argument(
        "-tu", "--top-authors", action="store_true",
        help="show the most popular authors of all time")

    group.add_argument(
        "-et", "--error-thresh", action="store_true",
        help="show the days where >1%% of requests led to errors")

    args = parser.parse_args()

    # Show help and exit if no arguments are provided
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)

    sys.exit(main(args))
