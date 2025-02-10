# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:03:14 2025

@author: J.B.pradeep kumar
"""

import numpy as np
import pickle 
import streamlit as st

# loading the saved model

loaded_model = pickle.load(open('trained_model 1.sav','rb'))

# creating afunction for prediction

def diabetic_predition(input_data):
    
    
    # changing the input data into numpy array

    input_data_as_array = np.asarray(input_data)

    # reshaping the array to a predicting for one instance

    input_data_reshape = input_data_as_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)

    print(prediction)

    if prediction[0] == 0:
      return 'The Patient is Non Diabetic'

    else:
      return 'The Patient is Diabetic'
  

def main():
    
    # giving a title 
    st.title('diabetis Prediction Web App')
    
    # getting the input data from the user
    
    Pregrancies = st.text_input('Number of Pregrancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure= st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Value')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
    
    
    # code for the Prediction
    
    diagnosis = ''
    
    # Creating a button for Prediction
    
    if st.button('Diabetic Test Result'):
        diagnosis = diabetic_predition([Pregrancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
    
    
    
    
if __name__=='__main__':
    main()
