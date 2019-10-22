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

```text
$ ./table-view.py org_accounts
+-----+-------+--------------+--------------+
| age | owner |  account_id  |     name     |
+-----+-------+--------------+--------------+
|  1  |  Liam | 123456789012 |  Production  |
|     |       | 733456499012 | Staging-Blue |
+-----+-------+--------------+--------------+
```

### Help Text `./table-view.py --help`

```text
usage: Table View [-h] [-ls] [--profile PROFILE] [--region REGION] [-v]
                  [dynamo_table]

positional arguments:
  dynamo_table       the DynamoDB table name or ID

optional arguments:
  -h, --help         show this help message and exit
  -ls                list all of the tables
  --profile PROFILE  the AWS profile to use
  --region REGION    the AWS region the instance is in
  -v, --verbose      increase output verbosity
```