# Compute the Pearson Correlation between the features 'Age' and 'JobInvolvement'
import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns

import logging
import io
import base64
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import your data into Python
# df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
script_path = os.path.join(os.path.dirname(__file__), '../data', "WA_Fn-UseC_-HR-Employee-Attrition.csv")
df = pd.read_csv(script_path)

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

# Save the plot to a buffer
buf = io.BytesIO()
pyplot.savefig(buf, format='png')
buf.seek(0)

# Encode the image in base64 and log it
img_base64 = base64.b64encode(buf.read()).decode('utf-8')
#logger.info("Scatter plot image (base64 encoded):")
#logger.info(f"data:image/png;base64,{img_base64}")

# Save the plot as a file
output_path = os.path.join(os.path.dirname(__file__), '../output', "boxplot.png")
# pyplot.savefig("../output/boxplot.png")
pyplot.savefig(output_path)
logger.info("Scatter plot saved as 'boxplot.png'")

# Close the buffer
buf.close()



