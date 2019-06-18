# Prediction

# Table of Contents

+ [1 Predict](#1-predict)
  + [1.1 Prediction Steps](#11-prediction-steps)
  + [1.2 Libraries](#12-libraries)
  + [1.3 Integration](#13-integration)
+ [2 Predict Data](#2-predict-data)
  + [2.1 Input Data](#21-input-data)
  + [2.2 Input Data Dictionary](#22-input-data-dictionary)
  + [2.3 Output Data](#23-output-data)
  + [2.4 Output Data Dictionary](#24-output-data-dictionary)

## 1 Predict

### 1.1 Prediction steps

*Detail the steps that the prediction process does*

### 1.2 Libraries
*List the libraries and the version of each one, that the predict process use*

|Library|Version|
|-------|-------|
|*Name of the library*|*Version*|

### 1.3 Integration

*Detail the aplication or area that will use the predictions, and how the project will be integrated with that.*

If to run the predict process we need an api request, please share here an example of the request and the detail about the parameters that we will need.

|Parameter|Detail|Example|
|---------|-------|------|
|*Name of the parameter*|*Definition of the parameter*|*Example*|


## 2 Predict Data

### 2.1 Input Data
*Which inputs read the predict? And where will each of them be located (S3, Redshift)?*

*List all the input data following the next table structure*

|Table Name|Table Format|AWS Location|Schema/S3 Path|Size|Project/BusinessArea|
|---|---|---|---|----|----|
|*Name of the Table*| *Is a database table, parquet file, csv file, etc.*  | *Where is the data Redshift or S3* | *Where is located, if is in Redshift the name of the schema, if is in S3 the path where is the file*|*Data Volume in MB or GB*|*Which Area or Business Area will use the output?*|

### 2.2 Input Data Dictionary
*Dictionary of the dataset that will be used in the prediction process*

|Table Name|Table Variable|Variable Format|Description|
|---|---|---|---|
|*Name of the table or file*|*List the variables*|*Format of the variable (Varchar, Integer, etc)*|*Description of the feature*|
### 2.3 Output Data
*Which outputs generate the predict? And where will each of them be located (S3, Redshift)?*

*List all the output data following the next table structure*

|Table Name|Table Format|AWS Location|Schema/S3 Path|Size|Project/BusinessArea|
|---|---|---|---|----|----|
|*Name of the Table*| *Is a database table, parquet file, csv file, etc.*  | *Where is the data Redshift or S3* | *Where is located, if is in Redshift the name of the schema, if is in S3 the path where is the file*|*Data Volume in MB or GB*|*Which Area or Business Area will use the output?*|

### 2.4 Output Data Dictionary
*Dictionary of the dataset result of the prediction process*

|Table Name|Table Variable|Variable Format|Description|
|---|---|---|---|
|*Name of the table or file*|*List the variables*|*Format of the variable (Varchar, Integer, etc)*|*Description of the feature*|
