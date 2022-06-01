import streamlit as st
import pandas as pd
from inference import make_prediction


def file_type_entry() -> None:
    st.header("Loan Prediction")
    file = st.file_uploader("upload file", type=["csv"])
    show_file = st.empty()
    if not file:
        show_file.info("Please upload a file".format(''.join(["csv"])))
        return
    prediction_file = pd.read_csv(file)
    st.dataframe(prediction_file)
    if st.button("Predict"):
        predict = make_prediction(prediction_file)
        st.dataframe(predict)


def ondemand() -> None:
    st.header("Loan Prediction")
    product_list = [st.text_input("Loan_ID"), st.selectbox("Gender", ["Male", "Female"]),
                    st.selectbox("Married", ["Yes", "No"]), st.selectbox("Dependents", ["0", "1", "2"]),
                    st.selectbox("Education", ["Graduate", "Non-Graduate"]),
                    st.selectbox("Self_Employed", ["Yes", "No"]), st.text_input("Applicant Income"),
                    st.text_input("CoApplicant Income"), st.text_input("Loan Amount"),
                    st.text_input("Loan Amount Term"), st.selectbox("Credit_History", ["1", "0"]),
                    st.selectbox("Property_Area", ["Urban", "Semi-Urban", "Rural"])]
    if st.button("Predict"):
        df = pd.DataFrame([product_list],
                          columns=['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                                   'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
                                   'Credit_History', 'Property_Area'])
        ondemand_prediction = make_prediction(df)
        if ondemand_prediction[0] == 'Y':
            st.success("Yes! Customer will return the loan")
        else:
            st.success("Oops! Customer will not return the loan")


if __name__ == "__main__":
    Select_type_entry = st.sidebar.selectbox("Select the type of input", ["Indiviual Entry","File Type"])
    if Select_type_entry == "File Type":
        file_type_entry()
    else:
        ondemand()
