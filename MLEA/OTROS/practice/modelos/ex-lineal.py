import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# 1. Load the data into a dataframe
df = pd.read_csv("https://raw.githubusercontent.com/iaolier/7021DATSCI/main/data/Hitters.csv")

# 2. Get the number of rows and columns
df.shape

# 3. Get a summary of the data using the `describe()` function
df.describe(include='all')
# 4. Drop the rows with missing values using the `dropna()` function
df.dropna()

#5. Plot the distribution of the `Salary` variable using a histogram

sns.histplot(df['Salary'])
plt.show()

#6. Plot a pairplot of the variables using the `pandas` module. Identify the variables that seem to be correlated with `Salary`.
#pd.plotting.scatter_matrix(df, alpha=0.2, figsize=(10, 10))
#plt.show()

# 7. Use the function `get_dummies()` from the `pandas` module to convert the categorical variables into dummy variables.
print(df.head())
x = pd.get_dummies(df, drop_first=True)  # drop_first: la primera variable categorica no le hace la conversión a numerica
print(x.head())

