from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn import metrics

loaded_data = datasets.load_boston()
data_X = loaded_data.data
print(data_X.shape)
data_y = loaded_data.target
X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("MSE:", metrics.mean_squared_error(y_test, y_pred))
predicted = cross_val_predict(model, data_X, data_y, cv=10)
print("MSE:", metrics.mean_squared_error(data_y, predicted))


