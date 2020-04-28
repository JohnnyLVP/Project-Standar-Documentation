# Training Documentation

*Here -> High level describe the training proccess of the project*

# Table of Contents

- [Training Documentation](#training-documentation)
- [Table of Contents](#table-of-contents)
  - [1. Training](#1-training)
    - [1.1 Machine Learning techniques](#11-machine-learning-techniques)
    - [1.2 Parameters](#12-parameters)
    - [1.3 Business Rules](#13-business-rules)
    - [1.4 Model Format](#14-model-format)
    - [1.5 Model Metrics](#15-model-metrics)
    - [1.6 Execution Frecuency](#16-execution-frecuency)
    - [1.7 Libraries](#17-libraries)
  - [2. Training Data](#2-training-data)
    - [2.1 Data Dictionary](#21-data-dictionary)
    - [2.2 Input Data](#22-input-data)


## 1. Training

### 1.1 Machine Learning techniques
*Detail of the model technique that the project use for training*

### 1.2 Parameters
*Detail of the parameters that the model need for the execution*

### 1.3 Business Rules
*Put the detail of all the businees rules that the model consider for the training*

### 1.4 Model Format
*In Which format the model is serialized?(Pickle, parquet, other binary format)*
*How is been stored the model file?*

### 1.5 Model Metrics
*Put here the metrics that the model has.*

### 1.6 Execution Frecuency
*Describe here the event that will trigger the training, or if the training has to be executed manually.*

### 1.7 Libraries
*List the libraries and the version of each one, that the training process use*

|Library|Version|
|-------|-------|
|*Name of the library*|*Version*|

## 2. Training Data
### 2.1 Data Dictionary
*Describe here each variable in the training dataset that will be used in the training proccess.*

|Variable|Description|Data Type|
|--------|-----------|---------|
|*Variable Name*|*Description of the variable*|*Data Type of the variable (Varchar, Integer, Boolean, etc)*|

### 2.2 Input Data
*Describe here the files that will be used in the training proccess and where are located.*

|TableName|Location|Data Volumen|
|---------|--------|------------|
|*Put the table name here*|*If is in S3 put the S3 key and if is in Redshit, put the schema*|*Put the size of the table or file*|
