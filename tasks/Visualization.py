# Sample Univariate Visualization in Python - Single Column

from pickle import FALSE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# set default theme
sns.set_theme()

# Import your data into Python
script_path = os.path.join(os.path.dirname(__file__), '../data', "WA_Fn-UseC_-HR-Employee-Attrition.csv")
df = pd.read_csv(script_path)
logger.info('\n')
logger.info(df.index)

# --------------------------------------- UNIVARIATE ANALYSIS ------------------------------

# 1.1 Box Plot
sns.boxplot(df['Age'])   # alternative is plt.boxplot(df['Age'])
plt.title('1. Box Plot of Age')
plt.show()
# 1.2 Bar chart for Attrition
sns.countplot(x='Attrition', data=df, palette='Set2')
plt.title('2. Count of Attrition')
plt.xlabel('Attrition')
plt.ylabel('Count')
plt.show()
# 1.3 Bar chart for Attrition
sns.countplot(x='Department', data=df, palette='Set2')
plt.title('3. Count of Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()
# 1.4 Histogram plot for Monthly Income
sns.histplot(df['MonthlyIncome'], bins=20, kde=True, color='blue')
plt.title('4. Distribution of MonthlyIncome')
plt.xlabel('MonthlyIncome')
plt.ylabel('Frequency')
plt.show()
# 1.5 countplot for Gender
sns.countplot(df['Gender'])
plt.title('5. Count Plot of Gender (Categorical)')
plt.show()

# # --------------------------------------- BIVARIATE ANALYSIS -----------------------------
#
plt.figure(figsize=(10, 6))
sns.swarmplot(x='Attrition', y='MonthlyIncome', data=df, palette='Set2')
plt.title('6. Swarm Plot of Monthly Income by Attrition Status')
plt.xlabel('Attrition')
plt.ylabel('Monthly Income')
plt.show()

sns.scatterplot(x='DistanceFromHome', y='JobSatisfaction', data=df, hue='Attrition', palette='Set2')
plt.title('7. Scatter Plot of Distance from home vs Job Satisfaction')
plt.show()

# #----------------------------- MULTIVARIATE ANALYSIS ----------------------------------

# Create a FacetGrid for Monthly Income and Age, conditioned on Attrition
g = sns.FacetGrid(df, col="Attrition", height=5, aspect=1)
g.map(sns.scatterplot, "Age", "MonthlyIncome", color="blue")
g.add_legend()
g.set_titles("Attrition: {col_name}")
g.set_axis_labels("Age", "Monthly Income")
plt.subplots_adjust(top=0.9)
g.fig.suptitle("8. Scatter Plot of Age vs. Monthly Income by Attrition Status")
plt.show()


sns.lmplot(x='TotalWorkingYears', y='MonthlyIncome', data=df, hue='Attrition', palette='Set2')
plt.title('9. Total Working Years and Monthly Income by Attrition Status')
plt.xlabel('Total Working Years')
plt.ylabel('Monthly Income')

plt.show()