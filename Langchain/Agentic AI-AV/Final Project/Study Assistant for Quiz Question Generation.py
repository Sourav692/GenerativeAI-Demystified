# Databricks notebook source
!pip install pypdf2
!pip install langchain==0.3.11
!pip install langchain-openai==0.2.12
!pip install langchain-community==0.3.11

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import pypdf2

# COMMAND ----------

from getpass import getpass

OPENAI_KEY = getpass('Please enter your Open AI API Key here: ')

# COMMAND ----------

import os

os.environ['OPENAI_API_KEY'] = OPENAI_KEY

# COMMAND ----------

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# COMMAND ----------

chatgpt = ChatOpenAI(model_name='gpt-4o-mini', temperature=0.0)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Read the PDF File

# COMMAND ----------

import pypdf2

# COMMAND ----------

import pypdf2
# Open the PDF file

with open("./Prompt Engineering .pdf", "rb") as file:
  reader = PyPDF2.PdfReader(file)
  # Extract text from all pages
  study_material = ""
  for page in reader.pages:
    study_material += page.extract_text()
  # Now `study_material` contains the text from the PDF
  print(study_material)

# COMMAND ----------


