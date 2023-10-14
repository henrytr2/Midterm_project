import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
st.markdown("# Insurance Charges Exploration")
with st.expander(  "# Why are we doing this?"):
    st.write("In a recent survey conducted by Gallup and West Health, an estimated 112 million Amercians (44%) struggle to pay for [healthcare](https://www.westhealth.org/press-release/112-million-americans-struggle-to-afford-healthcare/#:~:text=WASHINGTON%2C%20D.C.%20%E2%80%94%20Mar.,is%20not%20worth%20the%20cost)."
            " National health spending is over 4 trillion in this country, and current projections indicate it will continue to grow at an annual rate of 5.4%, topping $6.2 trillion by 2028. "
             " The goal of this application  at a future date is too allow the user to input information about themselves and determine factors that impact their insurance rate."
             " Please note that there are several factors that this dataset does not include that may contribute to the cost of insurance. ")
st.sidebar.write("[Github Repo](https://github.com/henrytr2/Midterm_project)")
st.sidebar.write("## Dataset Info")
st.sidebar.write("This dataset contains information about insurance charges across different regions of the United States.")
st.sidebar.write("Let's explore the data and see if we can find any interesting details!")
show_column_info = st.sidebar.checkbox("Show Column Info")
if show_column_info:
    column_info = {
        'age': 'Age of the insured person',
        'sex': 'Gender of the insured person (male or female)',
        'bmi': 'Body Mass Index (BMI) of the insured person',
        'children': 'Number of children or dependents covered by the insurance',
        'smoker': 'Whether the insured person is a smoker (Yes or No)',
        'region': 'Region in the United States of the insured person'
    }
    st.sidebar.write("## Column Information")
    for col, desc in column_info.items():
        st.sidebar.write(f"- **{col}**: {desc}")
# load data
insurance = pd.read_csv("insurance.csv")

click_here = st.selectbox('Please select the dataset:', ['Insurance'])

if click_here == 'Insurance':
    df1 = insurance
    st.write("Let's look at some of the Raw Data!")

data_preview = st.checkbox("View Data Table")
if data_preview:
    st.write("## Dataset Preview")
    st.write(insurance.head())
    
    # Check for missing values
    missing_values = df1.isnull().sum()
    st.write("### Missing Values")
    st.write(missing_values)
    st.write("*We see that there are no missing values.*")
df = df1

button1 = st.checkbox("Show Statistics")
if button1:
    st.write(df.describe())
cols = df.columns

st.write("## Data Visualization")

# Basic Dists 

show_age = st.checkbox("Age")
show_children =st.checkbox("Children")
show_sex =st.checkbox("Gender")
show_bmi =st.checkbox("BMI")
show_smoker =st.checkbox("Smoker")
show_region =st.checkbox("Region")




if show_age:
    fig = px.histogram(insurance, x='age', marginal='box', nbins=100, title='Distribution of Age',)
    fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)
    st.write("*We see that while there are individuals from all ages in the dataset, a larger number of 18 and 19 year olds than another other age. Let's keep this in mind when we think of other data.*")

if show_children:
    fig = px.histogram(insurance, x='children', marginal='box', nbins=64, title='Distribution of Children',)
    fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)
    st.write("*The most common amount of children in the dataset are that of zero. Also, we can see the overall distribution of the data is heavily right skewed.*")

if show_sex:
    fig = px.histogram(insurance, x='sex',  nbins=64, title='Distribution of Gender',)
    fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)
    st.write("*The proportion of males to females are very close. There are only 14 more males than females in the data.*")

if show_bmi:
    fig = px.histogram(insurance, x='bmi', marginal='box', nbins=64, title='Distribution of BMI',)
    fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)
    st.write("*The distribution of BMI is nearly guassian, which is to be expected in nature.*")
if show_smoker:
    fig = px.histogram(insurance, x='smoker', marginal='box', nbins=64, title='Distribution of Smokers',)
    fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)
    st.write("*There are fare greater non-smokers than smokers.*")
if show_region:
    fig = px.histogram(insurance, x='region', nbins=64, title='Distribution of Region',)
    fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)
    st.write("*The number of people in each region are close.*")

st.write("**What Variables do you want to investigate?** *please choose is scatter plot of both x and y are numerical, and a bar chart if one value is categorical* ")
x_val = st.selectbox('Variable on the x-axis?', cols)
y_val = st.selectbox('Variable on the y-axis?', cols)
z_val = st.selectbox('Do you want a hue?', cols)

button3 = st.button("Bar Chart")
if button3:
    st.write(f"Mean {y_val} by {x_val}")
    mean_data = df.groupby(x_val)[y_val].mean().reset_index()
    fig = px.bar(mean_data, x=x_val, y=y_val)
    st.plotly_chart(fig, use_container_width=True)

if st.button("Hide Bar Chart"):
    button3 = False

button4 = st.button("Scatter Plot")
if button4:
    scatter_fig = px.scatter(df, x=x_val, y=y_val, color=z_val)
    st.plotly_chart(scatter_fig, use_container_width=True)

if st.button("Hide Scatter Plot"):
    button4 = False


st.markdown("## Lets take a closer look at some data that may be interesting")


fig = px.histogram(insurance, x='charges', marginal='violin',  title='Distribution of Charges')
fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
st.plotly_chart(fig, use_container_width=True)
st.write("*Most Charges are below 20k*")


st.markdown("### Are children impacting the insurance charges?")
boxplot_fig = px.box(insurance, x='children', y='charges',color='children', title='Insurance Charges by Number of Children')
boxplot_fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
st.plotly_chart(boxplot_fig, use_container_width=True)
st.write("*The number of children do not really give us information on the charges, we can see that the data is close. Also there are several outliers*")
st.markdown("### Region?")
boxplot_fig = px.violin(insurance, x='region', y='charges',color='region', title='Insurance Charges by Region')
boxplot_fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
st.plotly_chart(boxplot_fig, use_container_width=True)
st.write("*Again, not really.*")

st.markdown("### So what is?")

scatter_fig = px.scatter(insurance, x='age', y='charges', color='smoker')
scatter_fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
st.plotly_chart(scatter_fig, use_container_width=True)

scatter_fig = px.scatter(insurance, x='bmi', y='charges', color='smoker')
scatter_fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
st.plotly_chart(scatter_fig, use_container_width=True)



st.markdown(" ## The culprit seams to be determined by if one is a smoker or not!")

st.write("***So, how many smokers are there in the dataset?***" )

fig = px.histogram(insurance, x='smoker', nbins=64, title='Distribution of Smokers',)
fig.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False))
st.plotly_chart(fig, use_container_width=True)

st.markdown('### So, what is next')
with st.expander(  "# Click here to see!"):
    st.write("The next step is to create a regression model based on the parameters in this dataset to help determine and predict charges for individuals!. ")












