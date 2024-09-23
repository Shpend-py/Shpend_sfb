import streamlit as st
import pandas as pd
import numpy as np


st.title('This is a title')
st.header('This is a header with a divider', divider='rainbow')
st.subheader('This is a subheader with a divider', divider='rainbow')

q1_sales = {
    "january": "100",
    "feburary": "200",
    "march": "300"
}
q2_sales = {
    "april": "400",
    "may": "500",
    "june": "600"
}

st.write(q1_sales)

q1_df = pd.DataFrame(q1_sales.items(),
                     columns=["Month", "Amount"]
                    )

q2_df = pd.DataFrame(q2_sales.items(),
                     columns=["Month", "Amount"]
                    )

st.table(q1_df)

st.dataframe(q1_df)

df = pd.DataFrame(q1_sales.items())

st.dataframe(df,hide_index=True)

chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

st.line_chart(chart_data, x="col1", y="col2", color="col3")

q2_df2=q1_df.astype(str)
q1_df2=q2_df.astype(str)
st.line_chart(q1_df)
st.area_chart(q1_df)
st.bar_chart([q1_sales.values(), q2_sales.values()])

if st.button("Show Q2 Data"):
    st.table(q2_df)
else:
    st.table(q1_df)
    
if st.checkbox("Show Q2 Data"):
    st.line_chart(q2_df2)
else:
    st.line_chart(q1_df2)
    
quarter = st.radio("Which Quarter?",("Q1","Q2"))

if quarter == "Q1":
    st.line_chart(q1_df2)
elif quarter == "Q2":
    st.line_chart(q2_df2)
    
select_quarters = st.selectbox("Which quarter",("Q1","Q2"))

if select_quarters == "Q1":
    st.line_chart(q1_df2)
elif select_quarters == "Q2":
    st.line_chart(q2_df2)
    
st.write(st.slider("Which quarters?", 1,4,(2)))

values = st.slider("Please select a range of values, 0.0, 100.0, (40.0, 80.0)")

st.write(values)

st.write(st.multiselect("Choose quarters",
                        ["Q1","Q2","Q3","Q4"]))

st.write(st.number_input("Which quarters",1,40))

if section == "Text":
    st.write("Loren inpsun")
elif section == "chsarts":
    st.write(q1_sales)
elif section == "Widget":
    st.write(st.slider("Simple Slider", 1, 4, (0)))
    
    