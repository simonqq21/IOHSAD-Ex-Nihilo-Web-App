#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 13:27:44 2021

@author: simonque
"""

# importing psycopg2
import psycopg2
  
conn=psycopg2.connect(
    database="testdb",
    user="simonque",
    password="12345678",
    host="localhost",
    port="5432"
)
  
  
# Creating a cursor object using the cursor() 
# method
cursor = conn.cursor()
  
# drop table accounts
sql = '''DROP TABLE simonque."Film" cascade '''
  
# Executing the query
cursor.execute(sql)
print("Table dropped !")
  
# Commit your changes in the database
conn.commit()
  
# Closing the connection
conn.close()