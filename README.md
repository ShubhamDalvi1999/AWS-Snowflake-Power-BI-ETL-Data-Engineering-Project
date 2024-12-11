<h2 align="center">
  Welcome to My AWS Data Pipeline and Analytics Project!
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28">
</h2>

<!-- Intro  -->
<h3 align="center">
        <samp>&gt; Hey There!, I am
                <b><a target="_blank" href="https://yourwebsite.com">Shubham Dalvi</a></b>
        </samp>
</h3>

<p align="center"> 
  <samp>
    <br>
    「 I am a data engineer with a passion for big data, distributed computing, cloud solutions, and data visualization 」
    <br>
    <br>
  </samp>
</p>

<div align="center">
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&random=false&width=435&lines=Spark+%7C+DataBricks+%7C+Power+BI+;Snowflake+%7C+Azure+%7C+AWS;3+yrs+of+IT+experience+as+Analyst+%40+;Accenture+;Passionate+Data+Engineer+" alt="Typing SVG" /></a>
</div>

<p align="center">
 <a href="https://linkedin.com/in/yourprofile" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="yourprofile"/>
 </a>
</p>
<br />

<!-- About Section -->
# About Me

<p>
 <img align="right" width="350" src="/assets/programmer.gif" alt="Coding gif" />
  
 ✌️ &emsp; Enjoy solving data problems <br/><br/>
 ❤️ &emsp; Passionate about big data technologies, cloud platforms, and data visualizations<br/><br/>
 📧 &emsp; Reach me: shubhamdworkmail@gmail.com<br/><br/>
</p>

<br/>
<br/>
<br/>

## Skills and Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-013243?style=for-the-badge&logo=matplotlib&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![VSCode](https://img.shields.io/badge/Visual_Studio-0078d7?style=for-the-badge&logo=visual%20studio&logoColor=white)

<br/>

## Project Overview

This project showcases the implementation of an **AWS-based ETL pipeline** for extracting, transforming, and analyzing data using modern cloud tools. By leveraging **AWS Lambda**, **AWS S3**, **AWS Glue**, and **Snowflake**, the pipeline provides an efficient and scalable solution for data processing and analytics. 

The architecture is designed to handle raw data ingestion, schema inference, transformation, and storage while enabling advanced analytics through platforms like **Power BI** and **Amazon Athena**.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Skills Demonstrated](#skills-demonstrated)
- [AWS Architecture](#aws-architecture)
- [Data Flow](#data-flow)
- [Usage Instructions](#usage-instructions)

## Technologies Used
- **AWS S3**: For storing raw and processed data.
- **AWS Glue**: For orchestrating ETL workflows and schema inference.
- **AWS Lambda**: For event-driven processing and transformations.
- **Amazon Athena**: For querying processed data on demand.
- **Snowflake**: As the data warehouse for structured storage and analytics.
- **Power BI**: For interactive visualizations and business intelligence.
- **Python**: For custom processing and scripting.

## Skills Demonstrated
- **Cloud Integration**: Leveraging AWS services to build scalable data solutions.
- **ETL Automation**: Automating data ingestion and transformation workflows using AWS Glue and Lambda.
- **Data Engineering**: Implementing data pipelines for structured and unstructured datasets.
- **Data Visualization**: Creating dashboards and insights using Power BI.
- **Schema Management**: Using Glue Data Catalog and Crawlers for schema inference.
- **Analytics Enablement**: Querying datasets through Amazon Athena and Snowflake.

## AWS Architecture

![AWS to snowflake](https://github.com/user-attachments/assets/a107675c-9d04-43c2-9c70-e802f196438d)

The architecture consists of the following components:
1. **Extract**:
   - **Spotify API/Source**: Raw data fetched using Python scripts.
   - **AWS S3 (Raw)**: Stores the raw data in a dedicated S3 bucket.
   - **AWS Lambda**: Automates data ingestion and triggers subsequent processes.
   - **AWS CloudWatch/EventBridge**: Monitors and triggers ETL workflows.

2. **Transform**:
   - **AWS S3 (Transformed)**: Stores intermediate and transformed data.
   - **AWS Glue**: Performs schema inference and data cataloging.

3. **Load**:
   - **AWS Glue Catalog**: Maintains metadata and schema for querying.
   - **Snowflake**: Acts as the central data warehouse for structured storage and analysis.

4. **Analytics**:
   - **Power BI**: Enables interactive dashboards and reporting.
   - **Amazon Athena**: Provides on-demand SQL querying of transformed data.

## Data Flow
1. **Data Ingestion**:
   - Raw data is fetched and uploaded to an AWS S3 bucket.
   - AWS Lambda triggers preprocessing workflows.

2. **Transformation and Schema Management**:
   - AWS Glue performs schema inference and data cleaning.
   - Transformed data is stored back into S3.

3. **Storage and Analytics**:
   - Final data is loaded into Snowflake for analysis.
   - Power BI is used to create insights and visualizations.

## Usage Instructions
1. Set up AWS resources:
   - Create S3 buckets for raw and processed data.
   - Configure AWS Glue jobs and Crawlers.
   - Deploy Lambda functions for data ingestion.

2. Integrate with Snowflake:
   - Configure Snowflake as the data warehouse.
   - Set up ETL workflows to load data into Snowflake.

3. Visualize data:
   - Use Power BI to connect to Snowflake or Athena.
   - Build interactive dashboards for analysis.

4. Monitor pipeline:
   - Use AWS CloudWatch/EventBridge to monitor pipeline activity and performance.

---
Feel free to contribute or reach out if you have any suggestions or improvements!
