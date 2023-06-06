import pandas as pd
import numpy as np

dataset = pd.read_csv('C:\\Users\\madhavan.bala\\Downloads\\Day_6\\titanicsurvival.csv')
# print(dataset.head())

income_set = set(dataset['Sex'])
print(income_set)
dataset['Sex'] = dataset['Sex'].map({ 'female': 0 , 'male' : 1 }).astype(int)
print(dataset.head())

#Segregate Dataset into X(Input/IndependentVariable) & Y(Output/DependentVariable)
X_value = dataset.drop('Survived',axis='columns')
Y_value = dataset.Survived

#Finding & Removing NA values from our Features X
print(X_value.columns[X_value.isna().any()])
X_value['Age'] = X_value['Age'].fillna(X_value['Age'].mean())
print(X_value['Age'].isna())

#Splitting Dataset into Train & Test
from sklearn.model_selection import train_test_split
X_train,Y_train,X_test,Y_test = train_test_split(X_value,Y_value,test_size=0.25,random_state=0)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,Y_train)

#Predicting, wheather Person Survived or Not
pclassNo = int(input("Enter Person's Pclass number: "))
gender = int(input("Enter Person's Gender 0-female 1-male(0 or 1): "))
age = int(input("Enter Person's Age: "))
fare = float(input("Enter Person's Fare: "))
person = [[pclassNo,gender,age,fare]]
result = model.predict(person)
print(result)


if result == 1:
  print("Person might be Survived")
else:
  print("Person might not be Survived")

#Prediction for all Test Dat
y_pred = model.predict(X_test)
# print(np.column_stack(y_pred,Y_test))

#Accuracy of our Model
from sklearn.metrics import accuracy_score
print("Accurancy of the model  :  ",accuracy_score(Y_test,y_pred)*100)
