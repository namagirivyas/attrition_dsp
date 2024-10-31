# Compute the Pearson Correlation between the features 'Age' and 'JobInvolvement'
import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import your data into Python
df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
 
# Convert dataframe into series
list1 = df['Age']
list2 = df['JobInvolvement']

# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
logger.info('Pearson correlation: %.3f' % corr)

# Pearson correlation: 0.205 (Moderate Positive correlation)
# Interpretaton:
# As the age of the patient increases, days of stay in hospital also increases
from matplotlib import pyplot
# pyplot.scatter(list1, list2)
# pyplot.show()

pyplot.figure(figsize=(10, 6))
sns.boxplot(data=df, x='JobInvolvement', y='Age', palette="Set2")
pyplot.title("Age Distribution by Job Involvement Level")
pyplot.xlabel("Job Involvement")
pyplot.ylabel("Age")
pyplot.show()



