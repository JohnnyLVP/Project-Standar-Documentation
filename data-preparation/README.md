* Cual es el pipeline de ejecucion
* Data que genera la preparacion de datos
input
*

## 1 Data Preparation pipeline

## 2 Input Data
*Which inputs are needed for the solution (CSVs, parameters, database, parquet files)? And where will each of them be located (S3, Redshift)?*

*List all the input data following the next*


|Table Name|Table Format|AWS Location|Schema/S3 Path|Size|
|---|---|---|---|---|
| *Name of the Table* | *Is a database table, parquet file, csv file, etc.*  | *Where is the data Redshift or S3* | *where is located, if is in Redshift the name of the schema, if is in S3 the path where is the file*|*Data Volume in MB or GB*||

### Metadata (output de data prep)

*List all the variables that the model will use for training and prediction*

*Example:*

|Model|Training/Prediction|Variable Name|Variable Description|Data Type|
|-----|-------------------|-------------|--------------------|---------|
|Offer Model|Training|Codpais|Is the Code of the country | varchar|
