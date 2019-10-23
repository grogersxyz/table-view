#!/usr/bin/env python3
import boto3
import argparse
import pprint
from prettytable import PrettyTable
from functools import reduce


def list_tables(client):
    tables = client.list_tables()['TableNames']
    for table_name in tables:
        print('+ {}'.format(table_name))


def display_table(client, table_name, sort_column, desc):
    items = client.scan(TableName=table_name)['Items']
    table = PrettyTable()
    headers = []
    for item in items:
        headers.extend(item.keys())
    headers = list(set(headers))
    headers.sort()
    table.field_names = headers
    for item in items:
        row = [''] * len(headers)
        for key in item.keys():
            row[headers.index(key)] = item[key][next(iter(item[key]))]
        table.add_row(row)

    if sort_column:
        table.sortby = sort_column
        table.reversesort = desc

    print(table)


def main():
    parser = argparse.ArgumentParser(prog='Table View')
    parser.add_argument(
        'table', nargs='?', help='the DynamoDB table name or ID', metavar='dynamo_table')
    parser.add_argument('-ls', action='store_true',
                        help='list all of the tables', )
    parser.add_argument('--profile', help='the AWS profile to use', type=str)
    parser.add_argument('--region', help='the AWS region the instance is in',
                        type=str, default='ap-southeast-2')
    parser.add_argument('--verbose', '-v',
                        help='increase output verbosity', action='store_true')
    parser.add_argument('--sort', help='the column to sort entries by')
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--ascending', action='store_true',
                       help='sort in an ascending order')
    group.add_argument('--descending', action='store_true',
                       help='sort in a decending order')

    args = parser.parse_args()

    client = boto3.session.Session(
        region_name=args.region, profile_name=args.profile).client('dynamodb')

    if args.ls:
        list_tables(client)
    elif args.table:
        display_table(client, args.table, args.sort, args.descending)
    else:
        print('\nPlease provide either a table name or use -ls to list all tables\n')
        parser.print_help()


if __name__ == '__main__':
    main()
