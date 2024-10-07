# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:42:06 2023

@author: DHEERAJ
"""

import numpy as np
import pickle
import streamlit as st

 #loading the saved model
loaded_model = pickle.load(open('C:/Users/DHEERAJ/Desktop/heart disease/trained_model.sav', 'rb'))

# creating a function for prediction
def heart_prediction(input_data):
    
    
  # change the input data to a numpy array
  input_data_as_numpy_array= np.asarray(input_data)

  # reshape the numpy array as we are predicting for only on instance
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

  prediction = loaded_model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0]== 0):
    return 'The Person does not have a Heart Disease'
  else:
    return 'The Person has Heart Disease'

def main():
    
    
    #giving a title
    st.title('Heart disease prediction app')
    
    
    #getting the input data from the user

    
    age = st.text_input('what is your age')
    sex = st.text_input('what is your sex') 
    cp = st.text_input('cp value')
    trestbps = st.text_input('trestbps value')
    chol = st.text_input('chol value')
    fbs = st.text_input('fbs value')
    restecg = st.text_input('restecg value')
    thalach = st.text_input('thalach value')
    exang = st.text_input('exang value')
    oldpeak = st.text_input('oldpeak value')
    slope = st.text_input('slope value')
    ca = st.text_input('ca value')
    thal = st.text_input('thal value')
    
    #code for prediction
    diagnosis = ''
    
    
    #creating a button for prediction
    
    if st.button('Heart disease result'):
        diagnosis = heart_prediction([age, sex, cp,	trestbps, chol,	fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
])
    
    st.success(diagnosis)
    
    
     
    
if __name__=='__main__':
        main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        