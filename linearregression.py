import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('HRPDataset.csv')

df.head()
df.shape

print('Defining x and y variables..')
x=df['Area']
y=df['Price']

plt.scatter(x,y,color='blue')

print('Splitting dataset into Training data and Testing data')
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0)

plt.scatter(x_train,y_train,color='green')
plt.scatter(x_test,y_test,color='red')

print('Training model using x_train and y_train')
lr = LinearRegression()
lr.fit(x_train.values.reshape(-1,1),y_train)

print('Predicting using trained model for values of x_test')
y_pred=lr.predict(x_test.values.reshape(-1,1))

print(y_train)
print(y_test)

plt.scatter(x_train,y_train,color='blue')
plt.scatter(x_test,y_test,color='cyan')