import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/iaolier/7021DATSCI/main/data/Auto.csv")

print(df.shape)  # Rows, columns
df["origin"] = df["origin"].astype('category')  # set type
print(df.dtypes)  # Types of columns
print(df.describe(include='all'))  # Basic measures

# =========================== Plotting ================================


def plotScatter():
    plt.scatter(df['cylinders'], df['mpg'])
    plt.xlabel('Cylinders')
    plt.ylabel('mpg')
    plt.show()


def plotBloxSeaB():
    sns.boxplot(x=df['cylinders'], y=df['mpg'])
    plt.show() # It works beacuse seaborn uses matplot


def pairplot():
    """
    Aquí uno mira las relaciones entre las variables: creciente, decreciente, no hay relación
    Cuando se compara la varibale con si misma se muestra un histograma
    :return:
    """
    pd.plotting.scatter_matrix(df, alpha=0.2, figsize=(10, 10))
    plt.show()


def histogram():
    sns.histplot(df['mpg'])
    plt.show()


def saveImg():
    sns.histplot(df['mpg'])
    plt.savefig("./../files/histograma.png")


saveImg()