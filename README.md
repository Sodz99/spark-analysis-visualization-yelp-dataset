# Spark Project-Analysis and Visualization on Yelp Dataset

Spark Project-Analysis and Visualization on Yelp Dataset — Big Data project.

## Overview
Yelp data encompasses user-generated content such as reviews, ratings, photos, and business information from the Yelp platform, which serves as a vital resource for consumers seeking local businesses and services. Processing Yelp data involves extracting, analyzing, and interpreting this wealth of information to derive actionable insights that can significantly benefit businesses.

By analyzing Yelp data, companies can understand customer preferences, identify strengths and weaknesses, and monitor competitive dynamics. This process helps businesses enhance their customer service, improve product offerings, and tailor marketing strategies to better meet consumer demands. Moreover, it provides an opportunity to gauge customer sentiment and address issues promptly, fostering a positive brand reputation.

## Approach
1)   Create an S3 bucket
2)   Create an EMR cluster with master and slave nodes, including Spark and Hive components
3)   Create OpenSearch domain
4)   Create AWS RDS instance
5)   Convert JSON files to CSV using Python scripts
6)   Upload CSV files to S3 bucket
7)   Use EMR to transfer CSV files to Amazon RDS
8)    Migrate data from RDS to HDFS (Hadoop Distributed File System) using EMR.
9)    Perform data transformations on the dataset in HDFS using Apache Spark.
10)   Perform mappings and indices using OpenSearch
11)   Create visualizations in OpenSearch

Architecture:

## Tech stack
➔ Language: Spark. ➔ Services: Amazon EMR, AWS RDS, AWS S3, HDFS, Amazon OpenSearch

Key Takeaways:

- Understanding the Yelp dataset
- Creating IAM user in AWS
- Creating S3 buckets
- Uploading data in S3 buckets
- Creating AWS RDS instance
- Creating an AWS EMR cluster
- Creating OpenSearch Domain
- Convert JSON files to CSV files
- Loading data to RDS
- Importing data from RDS to HDFS using Sqoop
- Performing data transformation using Spark
- Understanding OpenSearch Mappings and Indices
- Visualization in OpenSearch

## How to run

## Project structure
```
.gitignore
Codes/
  Codes/
    es_mappings.py
    index_data.py
    json_to_csv.py
README.md
```

## Credits
Based on a ProjectPro guided project.
