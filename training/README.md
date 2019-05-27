# Training Documentation

*Here -> High level describe the training proccess of the project*

# Table of Contents

* [1. Analitical Conceptual Architecture](1-Analitical-Conceptual-Architecture)
* [2. Training]()
  * [2.1. Machine Learning Techniques]()
  * [2.2. Parameters]()
  * [2.3. Business Rules]()
  * [2.4. Model Format]()
* [3. Training Data]()
  * [3.1. Data Dictionary]()
  * [3.2. Input Data]()

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

### 2.5 Frecuency
*Describe here the event that will trigger the training, or if the training has to be executed manually.*

## 3. Training Data
### 3.1 Data Dictionary
*Describe here each variable in the training dataset that will be used in the training proccess.*

|Variable|Description|Data Type|
|--------|-----------|---------|
|*Variable Name*|*Description of the variable*|*Data Type of the variable (Varchar, Integer, Boolean, etc)*|

### 3.2 Input Data
*Describe here the files that will be used in the training proccess and where are located.*

|TableName|Location|Data Volumen|
|---------|--------|------------|
|*Put the table name here*|*If is in S3 put the S3 key and if is in Redshit, put the schema*|*Put the size of the table or file*|
