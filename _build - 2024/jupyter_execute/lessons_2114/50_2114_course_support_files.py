#!/usr/bin/env python
# coding: utf-8

# # MSE 2114 Data Files

# ## Download links

# Files are stored in google drive and can be downloaded using the links in the list below.  

# Files in the order in which they show up in the textbook. 
# 
# |    Data Set Download Link   |    File Type     |   File ID  |
# | :-------------------------- | :------------   | :---------- |
# |[Titanic Data Set (csv file)](https://drive.google.com/uc?export=download&id=1ELCvnr0WjQcglNlmxhqzsAOK8DnPaHW_) |csv |  1ELCvnr0WjQcglNlmxhqzsAOK8DnPaHW_ |
# | | | |
# | | | |
# | | | |
# ---

# (Appendix_2114_Data_Files_direct)=
# ## Direct read code

# The data can also be downloaded directly into your notebook using the file url in place of the file path in our read statements.  Examples for different types of files are shown below.  

# Remember to make sure that you have run: `import pandas as pd` also these files **must already be shared** on google drive. 
# 
# * Excel file:  
# `pd.read_excel("https://drive.google.com/uc?id=14uBqZM8ekl1RoFgx3nwCJM7fe9N144RI")`  
# * CSV file:  
# `pd.read_csv("https://drive.google.com/uc?id=1ELCvnr0WjQcglNlmxhqzsAOK8DnPaHW_)`  
# * Compressed (ZIP) CSV file:  
# `pd.read_csv("https://drive.google.com/uc?id=1uBJd4eIZgYL38YyG4AZsbpGvBuH9KCsQ",compression='zip')`  
# * Google Sheet e.g. google form data responses:
# `pd.read_csv(https://docs.google.com/spreadsheets/d/13PLZ2N8txdPGn9P19VINPAMDup7ExLsh_Dso9_qLw0c/export?format=csv)`
# 

# In[ ]:




