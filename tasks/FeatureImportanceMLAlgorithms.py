# URL Ref - https://machinelearningmastery.com/calculate-feature-importance-with-python/
# For the HR Attrition Dataset, show the feature importance for:
# 1. Decision Tree - CART Feature Importance
# 2. Random Forest

import pandas as pd
from sklearn.model_selection import train_test_split
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

script_path = os.path.join(os.path.dirname(__file__), '../data', "WA_Fn-UseC_-HR-Employee-Attrition.csv")
df = pd.read_csv(script_path)
logger.info('\n')
logger.info(df)

from sklearn import preprocessing
import matplotlib.pyplot as plt

# Use Dummy Variables
df = pd.get_dummies(df, drop_first=True)

#  Attrition is the target variable.
selected_columns = ['Age', 'DistanceFromHome', 'JobSatisfaction', 'MonthlyIncome', 'WorkLifeBalance', 'YearsSinceLastPromotion']
X = df[selected_columns]
Y = df['Attrition_Yes']

#
# 1. Decision Tree
# Decision tree algorithms like classification and regression trees (CART) offer importance scores based on the reduction in the criterion used to select split points, like Gini or entropy.
# After being fit, the model provides a feature_importances_ property that can be accessed to retrieve the relative importance scores for each input feature.
from sklearn.tree import DecisionTreeClassifier
# define the model
model = DecisionTreeClassifier()
# fit the model
model.fit(X,Y)
# get importance
importance = model.feature_importances_

feature_importance_df = pd.DataFrame({
    'Feature': selected_columns,
    'Importance': importance
})
# sorted_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
logger.info('\n')
logger.info(feature_importance_df.sort_values(by='Importance', ascending=False))
logger.info('\n')

# plot feature importance
plt.bar([x for x in range(len(importance))], importance)
plt.show()

# 2. Random Forest Feature Importance
# After being fit, the model provides a feature_importances_ property that can be accessed to retrieve the relative importance scores for each input feature.

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

importances = model.feature_importances_

# Create a DataFrame for visualization
feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
})

# Sort the DataFrame by importance
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Plot feature importance
plt.figure(figsize=(10, 6))
import seaborn as sns
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Feature Importance from Random Forest')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()
