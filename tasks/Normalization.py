# Demo of Normalization -> Min-Max and Z-Score Normalization 

# 1. Apply Min-Max Normalization to 'Age' column in the Covid dataset; 
# So age ranges will be in the interval [0,1]

import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
script_path = os.path.join(os.path.dirname(__file__), '../data', "WA_Fn-UseC_-HR-Employee-Attrition.csv")
df = pd.read_csv(script_path)

df.head()

# copy the data
df_min_max_scaled = df.copy()

numerical_features = ['Age', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome']
from sklearn.preprocessing import MinMaxScaler

# Initialize the scaler
scaler = MinMaxScaler()

# Apply the scaler to the selected numerical features
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# Check the resulting DataFrame
logger.info('\n')
logger.info(df[numerical_features].head())

from sklearn.preprocessing import StandardScaler
logger.info('\nStandardization Z-score')
logger.info('\n')
# Initialize the scaler
scaler = StandardScaler()

# Apply the scaler to the selected numerical features
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# Check the resulting DataFrame
logger.info('\n')
logger.info(df[numerical_features].head())
