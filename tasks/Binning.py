# Discretization by Binning methods 
# Distance Binning and Frequency Binning

import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
logger.info(df)

# 1. Age Binning
# Formula -> interval = (max-min) / Number of Bins
age_bins = np.linspace(df['Age'].min(),df['Age'].max(),6)
logger.info(age_bins)
labels = ['Under 25', '25-35', '36-45', '46-55', '56+'];
df['Age_Bins'] = pd.cut(df['Age'], bins=age_bins, labels=labels)
logger.info(df['Age_Bins'])

# 2. Monthly income Binning
monthly_bins = np.linspace(df['MonthlyIncome'].min(),df['MonthlyIncome'].max(),5)
logger.info(monthly_bins)
labels=['Low', 'Medium', 'High', 'Very High']
df['MonthlyIncome_Bin'] = pd.cut(df['MonthlyIncome'], bins=monthly_bins, labels=labels)
logger.info(df['MonthlyIncome_Bin'])
