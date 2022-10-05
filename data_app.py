from asyncore import write
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Streamlit Web App")

st.header("Load Your CSV Data")

first_file_upload = st.file_uploader("Upload First File", type=["csv"])
second_file_upload = st.file_uploader("Upload Second File", type=["csv"])

if first_file_upload is not None and second_file_upload is not None:

    first_file = pd.read_csv(first_file_upload)
    second_file = pd.read_csv(second_file_upload)

    first_cols = first_file.columns.to_list()
    second_cols = second_file.columns.to_list()

    how = st.selectbox("Merge Method", options=["inner", "left", "right", "outer", "cross"])
    
    left_on = st.selectbox("Left On", options=first_cols)
    right_on = st.selectbox("Right On", options=second_cols)

    df = first_file.merge(second_file, how=how, left_on=left_on, right_on=right_on)

    st.write(df)

    if st.checkbox("Group Data"):

        df_cols = df.columns.to_list() 
        groupby = st.multiselect("Choose group by columns.", options=df_cols)
        value = st.selectbox("Choose a value for aggregation.", options=df_cols, key="value")
        aggregation_method = st.selectbox("Select aggreagtion method:", options=("Count", "Mean", "Sum"), key="agg_method")

        if aggregation_method == "Count":
            st.write(df.groupby(by=groupby)[value].count())
            #st.write("Count")
        elif aggregation_method == "Mean":
            st.write(df.groupby(by=groupby)[value].mean())
            #st.write("Mean")
        elif aggregation_method == "Sum":
            st.write(df.groupby(by=groupby)[value].sum())
            #st.write("Sum")
    else: 
        st.write("Data is ungrouped.")

else:
    st.write("Please Upload CSV Files")