import streamlit as st 
# Logic -1 preaparing Templet

st.title("🛣️ Ticket Price Estimation") 
st.subheader("Get an approximate cost for your journey")
from langchain_core.prompts import ChatPromptTemplate

# templet=ChatPromptTemplate(messages=[
#     ('system', 'You are an AI assistant for estimating average ticket price or cost.'),
#     ('human', 'Estimate and return the all types of classes average cost of traveling from {source} to {destination} using only {mode}.return only estimated avg costs of all classes.')])

templet=ChatPromptTemplate(messages=[
    ('system', 'You are an AI assistant for estimating average ticket price or cost and plan the trip.'),
    ('human', """Estimate and return the average cost breakdown for all travel classes from {source} to {destination} using only {mode} on this date {date}. Include the estimated average cost for each class and the overall estimated average cost of all classes. Format the response as follows:\n\nHere\'s an estimated average cost breakdown for different classes:
     \n- [Class Name]: price of that class 
     \n- [Class Name]: price of that class etc... 
     \nTherefore, the estimated average costs of all classes is: ₹[Overall Average].
     And return a trip plan explaing within 300 words.""")
])

#  Logic - 2 
from langchain_google_genai import ChatGoogleGenerativeAI
# with open(r"api_key.txt",'r') as key:
#     api_key=key.readline()
api_key="AIzaSyC9j5KaPVcanw9nvPAfKfORBqsCzBjx37I"
chat_model=ChatGoogleGenerativeAI(api_key=api_key,model="gemini-2.0-flash-exp")


# logic - 3
from langchain_core.output_parsers import StrOutputParser
output_parser=StrOutputParser()

s=st.text_input("Enter the Starting point: ")
d=st.text_input("Enter your destination: ")
m=st.text_input("Enter which mode do you want to travel: ")
date=st.date_input("select the date for your trip: ")
# s=input("enter starting point:")
# d=input("enter destination: ")
# m=input("enter which mode you want to travel: ")

raw_input={'source':s,"destination":d,"mode":m,"date":date}

chain= templet | chat_model | output_parser 
if st.button("Estimate"):
    result=chain.invoke(raw_input)
# print(result)
    st.write(result)

