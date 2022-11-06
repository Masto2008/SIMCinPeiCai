import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# startup_df = pd.read_csv('https://raw.githubusercontent.com/arib168/data/main/50_Startups.csv')
startup_df = pd.read_csv('Test1.csv')

shape=startup_df.shape
# print("Dataset contains {} rows and {} columns".format(shape[0],shape[1]))
# print(startup_df.columns)
#Statistical Details of the dataset
# print(startup_df.describe())
x=startup_df.iloc[:,:5]
y=startup_df.iloc[:,6]


print(x)
print(y)
#
from sklearn.preprocessing import OneHotEncoder
# ohe=OneHotEncoder(sparse=False)
# x=ohe.fit_transform(startup_df[['State']])
from sklearn.compose import make_column_transformer
col_trans=make_column_transformer(
    (OneHotEncoder(handle_unknown='ignore'),['v','d8','2c']),
    remainder='passthrough')
x=col_trans.fit_transform(x)
print(x)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=6)

#shapes of splitted data
print("X_train:",x_train.shape)
print("X_test:",x_test.shape)
print("Y_train:",y_train.shape)
print("Y_test:",y_test.shape)


linreg=LinearRegression()
linreg.fit(x_train,y_train)
y_pred=linreg.predict(x_test)
print(y_pred)

Accuracy=r2_score(y_test,y_pred)*100
print(" Accuracy of the model is %.2f" %Accuracy)

plt.scatter(y_test,y_pred);
plt.xlabel('Actual');
plt.ylabel('Predicted');
sns.regplot(x=y_test,y=y_pred,ci=None,color ='red');

pred_df=pd.DataFrame({'Actual Value':y_test,'Predicted Value':y_pred,'Difference':y_test-y_pred})
print(pred_df)
plt.show()