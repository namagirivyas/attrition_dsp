# Demonstrate One-hot encoding and Label encoding in Python
# 1. Importing the Libraries
import pandas as pd
import numpy as np
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 2. Reading the file
script_path = os.path.join(os.path.dirname(__file__), '../data', "WA_Fn-UseC_-HR-Employee-Attrition.csv")
df = pd.read_csv(script_path)
logger.info('\n')
logger.info(df)

#3. Apply Label encoding to the field 'Attrition'
# Import LabelEncoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# pd.set_option('display.max_columns', None)
df['Attrition'] = le.fit_transform(df['Attrition'])  # Converts 'Yes' to 1 and 'No' to 0
logger.info('\n')
logger.info(df['Attrition'])

# One-Hot Encoding for categorical columns
df = pd.get_dummies(df, columns=['Department', 'JobRole', 'Gender'], drop_first=True)

# Check the resulting DataFrame
logger.info('\n')
logger.info(df)

