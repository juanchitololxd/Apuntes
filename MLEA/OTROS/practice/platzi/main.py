import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler  # Para escalar los datos, minimizando errores al existir valores atípicos
from sklearn.linear_model import LinearRegression


class ModeloLinealUniVariado:
    def __init__(self):
        self._df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data", header=None,
                 sep="\s+")

        self._df.columns = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSDAT", "MEDV"]

        self._cols = ['DIS', 'INDUS', 'CRIM', 'RM', 'MEDV']  # Columns to predict
        sns.set(style='whitegrid', context='notebook')  # Styles

    def correlaciones(self):
        """
         Aqui Se ve que la mayor correlación directamente proporcional se da entre RM MEDV
         Si la correlación es negativa, es decir que es inversamente proporcional (como pasa con INDUS)
        """
        sns.heatmap(self._df[self._cols].corr(), cbar=True, annot=True, yticklabels=self._cols, xticklabels=self._cols)
        sns.pairplot(self._df[self._cols])

    def createModel(self):
        X = self._df[['RM']].values # Inputs. Se usa reshape si solo se accede a uan columna
        y = self._df[['MEDV']].values  # Output

        # Normalizar datos
        sc_x = StandardScaler()
        sc_y = StandardScaler()
        x_std = sc_x.fit_transform(X)
        y_std = sc_y.fit_transform(y)
        slr = LinearRegression()
        slr.fit(x_std, y_std)
        plt.xlabel("promedio de habitaciones")
        plt.ylabel("Mediana del precio de casas")
        # Se comparan los resultados con los valores reales
        plt.scatter(x_std, y_std)
        plt.plot(x_std, slr.predict(x_std), color='red')

        # Generate prediction using de model
        habitaciones = 5
        habitaciones_std = sc_x.transform(np.array([habitaciones]).reshape(-1, 1))
        valorCasa = sc_y.inverse_transform(slr.predict(habitaciones_std))
        print("El precio de una casa de {0} habitaciones es de {1} millones".format(habitaciones, valorCasa[0][0]))

    def showGraph(self):
        plt.show()


class ModeloLinealMultiVar(ModeloLinealUniVariado):
    def createModel(self):
        X = self._df[['RM', 'INDUS']].values  # Inputs. Se usa reshape si solo se accede a uan columna
        y = self._df[['MEDV']].values  # Output

        # Normalizar datos
        sc_x = StandardScaler()
        sc_y = StandardScaler()
        X_std = sc_x.fit_transform(X)
        y_std = sc_y.fit_transform(y)
        slr = LinearRegression()
        slr.fit(X_std, y_std)

        x1_range = np.arange(X_std[:, 0].min(), X_std[:, 0].max())
        x2_range = np.arange(X_std[:, 1].min(), X_std[:, 1].max())
        x1, x2 = np.meshgrid(x1_range, x2_range)

        pred = slr.predict(np.array([x1.flatten(), x2.flatten()]).T).reshape(x1.shape)
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x1, x2, pred, alpha=0.4, linewidth=2)
        ax.scatter3D(X_std[:, 0], X_std[:, 1], y_std, color='r', alpha=1)
        ax.view_init(elev=10, azim=5)
        ax.set_xlabel('RM')
        ax.set_ylabel('INDUS')
        ax.set_zlabel('MEDV')

"""
univar = ModeloLinealUniVariado()
univar.createModel()
univar.showGraph()

"""

multivar = ModeloLinealMultiVar()
multivar.createModel()
multivar.showGraph()

