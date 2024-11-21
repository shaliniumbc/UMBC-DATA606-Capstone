import streamlit as st
import pickle
import numpy as np

def loading_model():
    with open('app/saved_model.pkl','rb') as file:
        load_model=pickle.load(file)
    return load_model

data=loading_model()




def show_predict():
    st.title("Stock Price PREDICTION")
    st.write("""### *Fill out the form to predictStock price*""")

show_predict()

stocks = ["BAC",'AMZN']
HouseOwnership=st.selectbox("Stocks",stocks)

prev=st.number_input("Enter the previous price", min_value=0.0, max_value=1000.0, value=10.0)
day1change = st.number_input("Enter 1 day", min_value=-1000.0, max_value=1000.0, value=10.0)
day5avg=st.number_input("Enter avg of 5days",min_value=0.0,max_value=1000.0, value=0.0)
day10avg=st.number_input("Enter avg of 10days",min_value=0.0,max_value=1000.0, value=0.0)
day5vol=st.number_input("Enter vol of 5 days",min_value=0.0,max_value=1000.0, value=0.0)



result=st.button('Predict the Stock',key="red")
st.subheader("Prediction Results")
if result:
    x=np.array([[prev,day1change,day5avg,day10avg,day5vol]])
    x=x.astype(float)

    status=data.predict(x)
    st.success(f"the stock for next day for bank of america is {status}")

        
