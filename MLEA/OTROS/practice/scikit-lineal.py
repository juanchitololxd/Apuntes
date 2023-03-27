from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/iaolier/7021DATSCI/main/data/Hitters.csv', index_col=0)
df = df.dropna()
df = pd.get_dummies(df, drop_first=True)

lin_mdl = LinearRegression()  # Create multivariate linear object
X = df.drop('Salary', axis=1)  # inputs without output
y = df['Salary']  # only output

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # Data
lin_mdl.fit(X_train, y_train)  # Training model

y_pred = lin_mdl.predict(X_test) # prediction
print('Mean squared error: (MSE)', mean_squared_error(y_test, y_pred))
print(pd.Series(lin_mdl.coef_, index = X.columns)) # Print coefficients