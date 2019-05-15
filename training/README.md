# Training Documentation

*This is a template for python code*

# Table of Contents

* [1. Analitical Conceptual Architecture](1-Analitical-Conceptual-Architecture)
* [2. Training]()
  * [2.1. Machine Learning Techniques]()
  * [2.2. Parameters]()
  * [2.3. Business Rules]()
  * [2.4. Model Format]()
* [3. Data]()
  * [3.1. Input Data]()
  * [3.2. Output Data]()
  * [3.3. Data Variables Dictionary]()

## 1. Execution Flow Diagram
*Put the flow diagram for the execution*

*Flow diagram: Need to considerer all the steps for running the training and all the services that are related with the training.*

## 2. Training

### 2.1 Machine Learning techniques
*Detail of the model that the project use for training*

### 2.2 Parameters
*Detail of the parameters that the model need for the execution*

### 2.3 Business Rules
*Put the detail of all the businees rules that the model consider for the training*

### 2.4 Model Format
*In Which format the model is serialized?(Pickle, parquet, other binary format)*
*In which bucket of S3 will be upload the model?*

## 3. Data

### 3.1 Input
*Which inputs are needed for the solution (CSVs, parameters, database, parquet files)? And where will each of them be located (S3, Redshift)?*

*List all the input data following the next*


|Table Name|Table Format|AWS Location|Schema/S3 Path|Size|
|---|---|---|---|---|
| *Name of the Table*   | *Is a database table, parquet file, csv file, etc.*  | *Where is the data Redshift or S3* | *where is located, if is in Redshift the name of the schema, if is in S3 the path where is the file*|*Data Volume in MB or GB*||

### 3.2 Output
*Which outputs generate the model? And where will each of them be located (S3, Redshift)?*

*Which Project or Business Areas will use the data?*

*List all the input data following the next*

|Table Name|Table Format|AWS Location|Schema/S3 Path|Size|Project/BusinessArea|
|---|---|---|---|----|----|
|*Name of the Table*| *Is a database table, parquet file, csv file, etc.*  | *Where is the data Redshift or S3* | *Where is located, if is in Redshift the name of the schema, if is in S3 the path where is the file*|*Data Volume in MB or GB*|*Which Area or Business Area will use the output?*|

### 3.3 Data Variables Dictionary

*List all the variables that the model will use for training and prediction*

*Example:*

|Model|Training/Prediction|Variable Name|Variable Description|Data Type|
|-----|-------------------|-------------|--------------------|---------|
|Offer Model|Training|Codpais|Is the Code of the country | varchar|
