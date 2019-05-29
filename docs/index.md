## Table of Content

* [1 Redshift Best Practices](#1-redshift-best-practices)
* [2 Python Best Practices](#2-python-best-practices)
	* [2.1 Python Code Guide Lines](#21-python-code-guide-lines)
	* [2.2 AWS SDK for Python](#22-aws-sdk-for-python)
	* [2.3 Redshift Connection With Python](#23-redshift-connection-with-python)

## 1 Redshift Best Practices

### 1.1 Amazon Redshift Best Practices for Designing Queries<a name="c_designing-queries-best-practices"></a>

To maximize query performance, follow these recommendations when creating queries\.
+ Design tables according to best practices to provide a solid foundation for query performance\. For more information, see [Amazon Redshift Best Practices for Designing Tables](https://docs.aws.amazon.com/redshift/latest/dg/c_designing-tables-best-practices.html)\.
+ Avoid using `select *`\. Include only the columns you specifically need\.
+ Use a [CASE Expression](https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_CASE_function.html) to perform complex aggregations instead of selecting from the same table multiple times\.
+ Don’t use cross\-joins unless absolutely necessary\. These joins without a join condition result in the Cartesian product of two tables\. Cross\-joins are typically executed as nested\-loop joins, which are the slowest of the possible join types\.
+ Use subqueries in cases where one table in the query is used only for predicate conditions and the subquery returns a small number of rows \(less than about 200\)\. The following example uses a subquery to avoid joining the LISTING table\.

  ```
  select sum(sales.qtysold)
  from sales
  where salesid in (select listid from listing where listtime > '2008-12-26');
  ```
+ Use predicates to restrict the dataset as much as possible\.
+ In the predicate, use the least expensive operators that you can\. [Comparison Condition](https://docs.aws.amazon.com/redshift/latest/dg/r_comparison_condition.html) operators are preferable to [LIKE](https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_patternmatching_condition_like.html) operators\. LIKE operators are still preferable to [SIMILAR TO](https://docs.aws.amazon.com/redshift/latest/dg/pattern-matching-conditions-similar-to.html) or [POSIX Operators](https://docs.aws.amazon.com/redshift/latest/dg/pattern-matching-conditions-posix.html)\.
+ Avoid using functions in query predicates\. Using them can drive up the cost of the query by requiring large numbers of rows to resolve the intermediate steps of the query\.
+ If possible, use a WHERE clause to restrict the dataset\. The query planner can then use row order to help determine which records match the criteria, so it can skip scanning large numbers of disk blocks\. Without this, the query execution engine must scan participating columns entirely\.
+ Add predicates to filter tables that participate in joins, even if the predicates apply the same filters\. The query returns the same result set, but Amazon Redshift is able to filter the join tables before the scan step and can then efficiently skip scanning blocks from those tables\. Redundant filters aren't needed if you filter on a column that's used in the join condition\.

  For example, suppose that you want to join `SALES` and `LISTING` to find ticket sales for tickets listed after December, grouped by seller\. Both tables are sorted by date\. The following query joins the tables on their common key and filters for `listing.listtime` values greater than December 1\.

  ```
  select listing.sellerid, sum(sales.qtysold)
  from sales, listing
  where sales.salesid = listing.listid
  and listing.listtime > '2008-12-01'
  group by 1 order by 1;
  ```

  The WHERE clause doesn't include a predicate for `sales.saletime`, so the execution engine is forced to scan the entire `SALES` table\. If you know the filter would result in fewer rows participating in the join, then add that filter as well\. The following example cuts execution time significantly\.

  ```
  select listing.sellerid, sum(sales.qtysold)
  from sales, listing
  where sales.salesid = listing.listid
  and listing.listtime > '2008-12-01'
  and sales.saletime > '2008-12-01'
  group by 1 order by 1;
  ```
+ Use sort keys in the GROUP BY clause so the query planner can use more efficient aggregation\. A query might qualify for one\-phase aggregation when its GROUP BY list contains only sort key columns, one of which is also the distribution key\. The sort key columns in the GROUP BY list must include the first sort key, then other sort keys that you want to use in sort key order\. For example, it is valid to use the first sort key, the first and second sort keys, the first, second, and third sort keys, and so on\. It is not valid to use the first and third sort keys\.

  You can confirm the use of one\-phase aggregation by running the [EXPLAIN](https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_EXPLAIN.html) command and looking for `XN GroupAggregate` in the aggregation step of the query\.
+ If you use both GROUP BY and ORDER BY clauses, make sure that you put the columns in the same order in both\. That is, use the approach just following\.

  ```
  group by a, b, c
  order by a, b, c
  ```

  Don't use the following approach\.

  ```
  group by b, c, a
  order by a, b, c
  ```
**For more details, review the Redshift [Database Developer Guide](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html)**


## 2 Python Best Practices

### 2.1 Python Code Guide Lines

Python code should follow the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/).

Documentation follows the [Google documentation guidelines](http://google.github.io/styleguide/pyguide.html?showone=Comments#Comments). [Example](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

### 2.2 AWS SDK for Python

For working with the **AWS Services** in Python, we need to use the Boto3 Library.

if you have installed pip, you can install `boto3` executing as admin, the following script in the shell

```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3
```

#### 2.2.1 Python SDK for S3

For working with S3 and if you are in an EC2 Instance, and that instances has a IAM role associated, We use:

```python
import boto3
s3 = boto3.client('s3')
```

If we are working in a local machine, we have to add the `Access Key Id` and the `Secret Access Key` to the sentence:

```python
import boto3
s3 = boto3.client('s3',
	aws_access_key_id='<access-key-id>',
	aws_secret_access_key='<secret-access-key>')
```

* **List S3 Files**

Use this code line, when you want to list all files in a S3 path:

```python
for key in s3.list_objects(Bucket='<Bucket-Name>', Prefix = '<S3-Key-Path>')['Contents']:
    print(key['Key'])
```

For more details of using the `list_objects` function you can find it [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects).


* **Download S3 Files**
Use this code line, if you want to download some object from S3.

```python
s3.download_file(Bucket = '<Bucket-Name>',Key='<S3-Key>', Filename='<Local-Key>')
```
For more details of using the `download_file` function you can find it [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.download_file).


* **Upload S3 Files**
Use this code line, if you want to upload some file from your local machine to S3

```python
s3.upload_file(Filename = '<Local-Key>',Bucket ='<Bucket-Name>' ,Key = '<S3-Key>')
```

For more details of using the `upload_file` function, you can find it [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_file).


* **Delete S3 Files**
Use this code line, if you want to delete some file in S3.

```python
s3.delete_object(Bucket = '<Bucket-Name>', Key = '<S3-Key>')
```

For more details of using the `delete_object` function, you can find it [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.delete_object).

**There are more functions in the `Boto3` library, that you can use, you'll find it in the [Documentation Web Page](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)**


### 2.3 Redshift Connection with Python

For connecting to Redshift using python, we can use `psycopg2` library, that allow us to make query an executing from python.

if you have installed pip, you can install `psycopg2` executing as admin, the following script in the shell

```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org psycopg2
```

For connection, you can use this function:

```python
import psycopg2
def rs_connection(HOST,AWS_RS_PORT,AWS_RS_DATABASE,AWS_RS_USER,AWS_RS_PASS):
    '''
        Connection to Redshift
    '''
    con = psycopg2.connect(host=HOST,
                           port=AWS_RS_PORT,
                           dbname=AWS_RS_DATABASE,
                           user=AWS_RS_USER,
                           password=AWS_RS_PASS)

    cur = con.cursor()

    return cur,con
```

for querying, you can use the following script:

```python
def qry_redshift(rs_variable):

    cur,con = rs_connection('<rs_host>','<rs_port>','<rs_database>','<rs_user>','<rs_pass>')

    qry_load = '''
                select * from clients_table
                where date >= %(variable)s;   
    '''

    select_param = {'variable': rs_variable}

    cur.execute(qry_load, select_param)
    con.commit()
```

* Copy Command with Python

	If you want to execute the `copy command` using Python, you can use the following function:

```python
def CopyTables(s3_path, access_key_id, secret_access_key):

    cur, con = rs_connection('<rs_host>','<rs_port>','<rs_database>','<rs_user>','<rs_pass>')

    qry_load = '''
                copy <table_name>
                from %(s3_path)s
                access_key_id %(s3_key_id)s
                secret_access_key %(s3_secret_key)s
                delimiter ';'
                removequotes;
            '''

    select_param = {'s3_path': s3_path,
                    's3_key_id': access_key_id,
                    's3_secret_key': secret_access_key}

    cur.execute(qry_load, select_param)
    con.commit()
```
If you want to add more functions of the copy command you can check the [Copy Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html)


* Unload Command with Python
If you want to execute the `unload command` using Python, you can use the following function:

```python
def UnloadTables(s3_path, access_key_id, secret_access_key):

	cur, con = rs_connection('<rs_host>','<rs_port>','<rs_database>','<rs_user>','<rs_pass>')

	qry_load = '''
			unload ($$ select * from <table> where <condition> $$)
			to %(s3_path)s
			access_key_id %(s3_key_id)s
			secret_access_key %(s3_secret_key)s
			delimiter ';'
			addquotes
			parallel off
			maxfilesize 256 mb;
		'''

	select_param = {'s3_path': s3_path,
			's3_key_id': access_key_id,
			's3_secret_key': secret_access_key}

	cur.execute(qry_load, select_param)
	con.commit()
```
If you want to add more functions of the unload command you can check the [Unload Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_UNLOAD.html)
