import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Test1.csv', index_col = False)
print(data.describe())

#machine learning
X = data[["d8","c","2c"]]
y = data[["m"]]
print(X)
print(y)
regress = LinearRegression()
regress.fit(X,y)
print(regress.coef_)

#coefficentcy should be around 5 or -5

print(regress.intercept_)

newX = [[0.5,8,18]]
newY=regress.predict(newX)
print(newY)



# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
# columns = ["", ""]
# df = pd.read_csv("Test1.csv", usecols=columns)
# print("Contents in csv file:", df)
# plt.plot(df.Name, df.Marks)
# plt.show()