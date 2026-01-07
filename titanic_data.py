import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
titanic_df = pd.read_csv('Titanic.csv')

# Plot FacetGrid plot
plt.figure()
fg = sns.FacetGrid(titanic_df, row='Sex', col='Pclass', hue= "Survived", margin_titles=True)
fg.map(sns.scatterplot, 'Age', 'Fare')
fg.add_legend()
plt.show()
plt.close()