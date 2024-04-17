Cascade_Project
Part One: Identifying the Problem	1
Part Two: Designing the Solution	1



**Part One** Identifying the Problem
There is this criminal, Carmen Sandiego. Interpol has information from this woman from its agents all around the world. But the data is in ancient excel format. I want to turn it into CSV and after I prepare the infrastructure, I make some data requests from it. For example making queries, making views, etc.


**Part Two** Designing the Solution
My solution architecture has two parts;
**→Logical part (Logical workflow)**
Task 1: I want to extract the data from excel. Turn the original excel format into csv. 

Approach one: Using pandas for Data Extraction and Transformation
Step1→Extract Data from Excel Workbook: Use Python libraries such as pandas to read the Excel workbook and extract data from each sheet into DataFrame objects.
Step2→Standardize Column Names: Ensure that the column names in each DataFrame match the common data dictionary provided. You may need to rename columns accordingly.
Step3→Combine Data from Different Sheets: Concatenate or merge DataFrames from each region into a single DataFrame.
Step4→Data Cleaning and Transformation: Perform any necessary data cleaning and transformation tasks, such as handling missing values, converting data types, etc.
Step5→Export Data: Finally, export the cleaned and transformed DataFrame into a new CSV file or another suitable format for further analysis.

Approach two: Using dbt for Data Transformation
Step 1→Extract Data from Excel Workbook
Step 2→Create a Common Data Dictionary
Step 3→Develop Separate Models for Each Region (Repeat this step for each region, creating a separate model file for each.)

Approach three: Hybrid Data Processing with pandas and dbt
Step 1→Read Excel Sheets into Pandas DataFrames
Step 2→Save DataFrames as CSV Files in dbt Seeds Directory

Task2: 
The goal is to transform the data from each source into the common data dictionary format.
CTE Method: We'll write SQL code using CTEs to transform the data from each region's Excel sheet into the common format. Each CTE will represent a step in the transformation process.

Macros Method: We'll create reusable macros to handle common transformations, such as parsing dates or manipulating strings. These macros will make our models more efficient and easier to maintain.

Jinja Method: We'll use Jinja templating to make our models more generic, so they can adapt to different source data structures. We'll use placeholders for column names or conditions that may vary between regions.

Task4: 
Step 1: Identify the Three Most Occurring Behaviors
Step 2: Calculate the Probability of Each Behavior for Each Month
Step 3: Create Analytical Views

**→Technical part (Tech infrastructure)**
Task1: 
Approach one: run this code: XLtoCSV.py

Approach two: 
→In dbt directory, in models/common/ path, make data_dictionary.sql
→In dbt directory, in models/regions path, make 8 region sql files: region1.sql … region8.sql

→In terminal run commands from task1_bash_code file.

Approach three: 
→Run this pandas code for Data Extraction and Transformation: Data_Extraction_Transformation.py
→In dbt directory, in models/regions path, make 8 region sql files: region1.sql … region8.sql
→run this command: approachThree_bash

Task2: 
CTE Method
→Create a new SQL file in dbt project's models/ directory: transform_europe_data.sql
→run this command from root directory of dbt project: dbt run

Macros Method: 
→Define Common Data Dictionary sql file in models/common/ directory path: data_dictionary.sql
→create this sql file in the macros/ directory of the dbt project: transformation_macros.sql
→create sql file to Transform Data for Each Region in the models/regions directory: region1.sql … region8.sql
→run this command from root directory of dbt project: dbt run

Jinja Method: 
→Define Common Data Dictionary sql file in models/common/ directory path: data_dictionary.sql
→create sql file to Transform Data for Each Region in the models/regions directory: region1.sql … region8.sql
→Create Jinja Context File in the models/regions directory to define the Jinja context for each Region: region1.yml
→run this command from root directory of dbt project: dbt run



Task3: 
→create two sql files: schema.sql  ,  populate-schema.sql
Sighting
Location
Perpetrator
sighting_id  
date_witness 
Witness
Agent
Date_agent
city_agent
Location_id
Country
City
Latitude
longitude 
Perpetrator_id
Has_weapon
Has_hat
Has_jacket
behavior



Task4: 
A→Calculate the Probability of Carmen Sandiego Being Found in Each Agency Region for Each Month:  a_agency_region_by_month.sql
B→Calculate the Probability of Carmen Sandiego Being Armed, Wearing a Jacket, but Not a Hat for Each Month: b_carmen_sandiego_probabilities.sql
C→ Identify the Three Most Occurring Behaviors of Carmen Sandiego: c_most_common_behaviors.sql
D→Calculate the Probability of Carmen Sandiego Exhibiting One of Her Three Most Occurring Behaviors for Each Month: d_monthly_behavior_probability.sql

******************************************************************************

