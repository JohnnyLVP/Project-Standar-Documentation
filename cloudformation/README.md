# CloudFormation Templates
In this folder we will find all the services that the aplication ***Aplication-Name*** will need to be deployed.

# Table of Contents

* [1. Deploy](1-Deploy)
  * [1.2 AWS Services](1.2-AWS-Services)
* [2. Setup](2-Setup)
  * [2.2 AWS Services](2.2-AWS-Services)


## 1. Deploy

*Here will explain al the Templates that there are in the Deploy Folder.*
***In this folder, we have all the services that will have to re-deploy if we have any changes.***

### 1.2 AWS Services

*List the services that the project use in the deploy part and put details of each services*

*For Example:*

* EMR

|Env|Node Type|Instance Type|Number of Nodes|Instance Option
|----|---|---------|-----|------|
|QA|Master|*Example: m4.xlarge*|*Example: 1*|*Example: On-Demand*|
|QA|Core|*Example: m4.xlarge*|*Example: 1*|*Example: Spot*|


* Lambda

|Env|Lambda Function Name|Functionality|
|---|--------------------|-------------|
|QA|*Example: Lambda-qa-submit*|*Example: dispatch the submit in the EMR*|



## 2. Setup

*Here will explain al the Templates that there are in the Setup Folder.*
***In this folder, we have all the services that will deploy once.***

### 2.2. AWS Services

*List the services that the project use in the setup part and put details of each services*

*For Example:*

* SNS

|Env|SNS Name|Functionality|
|---|--------------------|-------------|
|QA|*Example: SNS-qas*|*Example: Send Notification ... *|


* SQS


|Env|SQS Name| Queue Type|Functionality|
|---|--------|-----------|-------------|
|QA|*Example: SQS-qas-type*|*Example: Standar Queue*|*Example: ..*|


* S3


|Env|Bucket Name|
|---|-----------|
|QA|* Example: ROD-belc-Bucket-qas*|
|PRD|* Example: ROD-belc-Bucket-prd*|


* IAM Roles

|Env|Role Name|Policies|
|---|--------|-----|
|QAs|*Example: ROD-Role*|*Example: S3 List, S3 PutObject, etc*|

## 3. Comments

If we need to consider something aditional for the deployment of the services and something related with the templates, please explain here.
