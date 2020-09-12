# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kiTFbOWEmSkmxue54-CRzOnX-a_fMvP3
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading the dataset from the drive
dataset=pd.read_csv('/content/drive/My Drive/Project/datasets_729058_1265963_Churn_Modelling.csv')

#using the columns with meaningfull data
x=dataset.iloc[:,3:13]
y=dataset.iloc[:,13]

#creating dummies for categorical columns
geography=pd.get_dummies(x['Geography'],drop_first=True)
gender=pd.get_dummies(x['Gender'],drop_first=True)


#concating the column to the table and removing the previous column
x=pd.concat([x,geography,gender],axis=1)

x=x.drop(['Geography','Gender'],axis=1)


#importing train test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#importing standardscaler to scale the data
from sklearn.preprocessing import StandardScaler 
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)







#importing keras
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU,PReLU,ELU
from keras.layers import Dropout

#creating object
classifier=Sequential()

#creating hidden layers
classifier.add(Dense(6,kernel_initializer='he_uniform',activation='relu',input_dim=11))

classifier.add(Dense(6,kernel_initializer='he_uniform',activation='relu'))

classifier.add(Dense(1,kernel_initializer='glorot_uniform',activation='sigmoid'))

classifier.compile(optimizer='Adamax',loss='binary_crossentropy',metrics=['accuracy'])

model_history=classifier.fit(x_train,y_train,validation_split=0.33,batch_size=10,epochs=100)

#getting the predictions
y_pred=classifier.predict(x_test)
y_pred=(y_pred>0.5)

#testing the accuracy of the model
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score 
score=accuracy_score(y_pred,y_test)



