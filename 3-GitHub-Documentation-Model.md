# Code Documentation

*This is a template for python code*

# Table of Contents

* [1. Analitical Conceptual Architecture](1-Analitical-Conceptual-Architecture)
* [2. Machine Learning Techniques]()
* [3. Data]()
  * [3.1 Input Data]()
  * [3.2 Output Data]()
* [4. Manual]()
* [5. Reported Bugs]()
* [6. Acknowledgements]()

## 1. Analitical Conceptual Architecture
*Put detail about the Conceptual architecture of the project in a diagram*
*Explain the flow that the Machine Learning model will do, to understad each step*

## 2. Machine Learning Techniques
*List in order the Machine Leaning techniques that are involved in the process.*

*For the ones that import from a library, indicate its name.*

## 3. Requirements

### 3.1. Programming Language and Installation

*Put the language that the model is using and the dependencies that need to be installed for use the language*

### 3.2. Libraries

*All the libraries and its versiones, that the model use.*

## 3. Data

### 3.1 Input
*Which inputs are needed for the solution (CSVs, parameters, database, parquet files)? And where will each of them be located (S3, Redshift)?*

*List all the input data following the next*


|Table Name|Table Format|AWS Location|Schema/S3 Path|
|---|---|---|---|
| *Name of the Table*   | *Is a database table, parquet file, csv file, etc.*  | *Where is the data Redshift or S3* | *where is located, if is in Redshift the name of the schema, if is in S3 the path where is the file*   |

### 3.2 Output
*Which outputs generate the model? And where will each of them be located (S3, Redshift)?*

*Which Project or Business Areas will use the data?*

*List all the input data following the next*

|Table Name|Table Format|AWS Location|Schema/S3 Path|
|---|---|---|---|
|*Name of the Table*| *Is a database table, parquet file, csv file, etc.*  | *Where is the data Redshift or S3* | *Where is located, if is in Redshift the name of the schema, if is in S3 the path where is the file*   |

### 3.3 Data Variables Dictionary

*List all the variables that the model will use for training and prediction*

*Example:*

|Model|Training/Prediction|Variable Name|Variable Description|Data Type|
|-----|-------------------|-------------|--------------------|---------|
|Offer Model|Training|Codpais|Is the Code of the country | varchar|


## 4. Manual

*Instructions for executing the solution locally. Which scripts need to be run? *

*If the solution is executed from terminal, offer an example of how to execute the scripts.*

```python
print("Example Here!")
```

## 5. Reported Bugs
*List and short explanation of all the bugs that have been reported*

## 6. Acknowledgements
*Any other optional acknowledgements the authors wish to make.*
