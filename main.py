import streamlit as st
import pickle
import numpy as np
pickle_in = open('CFD.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()
def prediction(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,AMOUNT):
    #input = np.array([[Amount,Classes]]).astype(np.float64)
    #prediction = model.predict(input)

    #return int(prediction)
    prediction = classifier.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,AMOUNT]])

    if prediction == 0:
        pred = 'NORMAL'
    else:
        pred = 'FRAUD'
    return pred

def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> CREDIT CARD FRAUD DETECTION </h1> 
    </div> 
    """
    # image = Image.open('lppppp.png')
    # st.image(image, caption='Loan Prediction')

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
   # TIME = st.slider("TIME",150,81000)
    V1 = st.slider("V1", -5.6, 2.45)
    V2 = st.slider("V2", -7.27, 8.3)
    V3 = st.slider("V3", -4.8, 9.3)
    V4 = st.slider("V4", -5.6, 1.68)
    V5 = st.slider("V5", -1.13, 3.48)
    V6 = st.slider("V6", -2.61, 7.33)
    V7 = st.slider("V7", -4.33, 1.20)
    V8 = st.slider("V8", -7.32, 2.32)
    V9 = st.slider("V9", -1.34, 1.55)
    V10 = st.slider("V10", -2.45, 2.37)
    V11 = st.slider("V11", -2.45, 3.21)
    V12 = st.slider("V12", -2.13, 1.20)
    V13 = st.slider("V13", -1.05, 2.63)
    V14 = st.slider("V14", -4.20, 3.25)
    V15 = st.slider("V15", -1.68, 4.32)
    V16 = st.slider("V16", -3.97, 2.5)
    V17 = st.slider("V17", -1.24, 5.23)
    V18 = st.slider("V18",-3.87,4.58)
    V19 = st.slider("V19", -1.32, 2.39)
    V20 = st.slider("V20",-2.54,5.69)
    V21 = st.slider("V21", -3.48, 2.72)
    V22 = st.slider("V22", -1.09, 1.05)
    V23 = st.slider("V23", -4.48, 2.25)
    V24 = st.slider("V24", -2.83, 4.58)
    V25 = st.slider("V25", -1.02, 7.51)
    V26 = st.slider("V26", -2.60, 3.51)
    V27 = st.slider("V27", -2.25, 3.16)
    V28 = st.slider("V28", -1.45, 3.38)
    AMOUNT = st.slider("AMOUNT OF TRANSACTION", 0, 25691)




    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,AMOUNT)
        st.success('TRANSACTION is {}'.format(result))



if __name__ == '__main__':
    main()




