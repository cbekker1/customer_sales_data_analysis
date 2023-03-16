# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:32:32 2023

@author: cleof
"""

#%% IMPORT MODULES

import pandas as pd
import psycopg2

#%% EXTRACT
excel_file = "G:/My Drive/2. Career Development/3. Applications/ShopriteX/assign_3.xlsx"



# read in the 'cat_sales' sheet into a pandas dataframe
cat_sales_df = pd.read_excel(excel_file, sheet_name="cat_sales")

# read in the 'cust_sales' sheet into a pandas dataframe
cust_sales_df = pd.read_excel(excel_file, sheet_name="cust_sales")

#%% TRANSFROM 
 


#%% LOAD part 1

db_params = {
    "host": "localhost",
    "port": 32768,
    "database": "postgres",
    "user": "postgres",
    "password": "postgrespw",
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

cur.execute("""CREATE TABLE if not exists cust_sales (
    period varchar(255),
    scenario varchar(255),
    member_id varchar(255),
    article_code varchar(255),
    article_desc varchar(255),
    category_group_no bigint,
    category_group_desc varchar(255),
    sales bigint
);
""")

cur.execute("""
CREATE TABLE if not exists cat_sales (
    category_group_no bigint,
    category_group_desc varchar(255),
    sales bigint
);
""")


# %% LOAD part 2


# Define the table name and column names
table_name = "cat_sales"
col_names = ["category_group_no", "category_group_desc", "sales"]

# Iterate over the rows in the Pandas DataFrame and insert them into the database
for row in cat_sales_df.itertuples(index=False):
    values = [getattr(row, col) for col in col_names]
    cur.execute(f"INSERT INTO {table_name} ({', '.join(col_names)}) VALUES ({', '.join(['%s']*len(values))})", values)

conn.commit()

table_name = "cust_sales"
col_names = ["period", "scenario", "member_id", "article_code", "article_desc", "category_group_no","category_group_desc","sales"]
for row in cust_sales_df.itertuples(index=False):
    values = [getattr(row, col) for col in col_names]
    cur.execute(f"INSERT INTO {table_name} ({', '.join(col_names)}) VALUES ({', '.join(['%s']*len(values))})", values)

# Commit the transaction and close the cursor and connection
conn.commit()
cur.close()
conn.close()