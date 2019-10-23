# Table View

View simple DynamoDB tables from the command line

## Instillation

1. Install the requirements using `pip install -r requirements.txt`
2. Run one of the commands below

## Examples

### List Tables `./table-view.py -ls`

```text
$ ./table-view.py -ls
+ org_accounts
+ users
+ groups
```

### View Table `./table-view.py <table_name>`

Columns are ordered alphabetically

```text
$ ./table-view.py org_accounts
+--------------+-----+--------------+-------+
|  account_id  | age |     name     | owner |
+--------------+-----+--------------+-------+
| 123456789012 |  1  |  Production  |  Liam |
| 733456499012 |     | Staging-Blue |       |
+--------------+-----+--------------+-------+
```

You can sort by a column name as well by passing the column name to `--sort`.
By default it will sort in `--ascending/--asc` order, you can also sort by `--descending/--des` order.

```text
$ ./table-view.py org_accounts --sort name --des
+--------------+-----+--------------+-------+
|  account_id  | age |     name     | owner |
+--------------+-----+--------------+-------+
| 733456499012 |     | Staging-Blue |       |
| 123456789012 |  1  |  Production  |  Liam |
+--------------+-----+--------------+-------+
```

### Help Text `./table-view.py --help`

```text
usage: Table View [-h] [-ls] [--profile PROFILE] [--region REGION] [--verbose]
                  [--sort SORT] [--ascending | --descending]
                  [dynamo_table]

positional arguments:
  dynamo_table       the DynamoDB table name or ID

optional arguments:
  -h, --help         show this help message and exit
  -ls                list all of the tables
  --profile PROFILE  the AWS profile to use
  --region REGION    the AWS region the instance is in
  --verbose, -v      increase output verbosity
  --sort SORT        the column to sort entries by
  --ascending        sort in an ascending order
  --descending       sort in a decending order
```
