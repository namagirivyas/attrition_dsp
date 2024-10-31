import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure standard logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load the dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
#print(df)
logger.info("Dataset loaded successfully.")
logger.info(f"DataFrame head:\n{df.head()}")

# # Convert date columns to datetime format
# There are no date specific fields to be handled

# Summary statistics
logger.info("\nSummary Statistics:")
pd.set_option('display.max_columns', None)
logger.info(df.describe(include='all'))
pd.reset_option('display.max_columns')

# Checking for missing values
logger.info("\nMissing Values:")
logger.info(df.isnull().sum())

# Data type information
logger.info("\nData Types:")
logger.info(df.dtypes)

# Attrition values from given dataset
attrition_counts = df['Attrition'].value_counts()
# logger.info("\nAttrition:")
logger.info(attrition_counts)
