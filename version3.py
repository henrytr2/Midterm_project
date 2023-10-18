import pandas as pd
import streamlit as st
import plotly.express as px
import hiplot as hip
import altair as alt


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'times', sans-serif;
			}
			</style>
			"""
# load data
insurance = pd.read_csv("insurance.csv")
df1 = insurance
st.markdown(streamlit_style, unsafe_allow_html=True)

st.image('hi.jpg')
cols=st.columns(3,gap='large')
with cols[0].expander("CNN:"):
    st.video("https://www.youtube.com/watch?v=wO-DAdZX59w",start_time=0)
with cols[1].expander("Consumer Reports:"):
    st.video("https://www.youtube.com/watch?v=DBTmNm8D-84",start_time=0)
with cols[2].expander("WSJ:"):
    st.video("https://www.youtube.com/watch?v=t7RiQbjlOfQ",start_time=0)
st.sidebar.write("[Github Repo](https://github.com/henrytr2/Midterm_project)")
st.sidebar.write("## Dataset Info")
st.sidebar.write("This dataset contains information about insurance charges across different regions of the United States.")
st.sidebar.write("Let's explore the data and see if we can find any interesting details!")
show_column_info = st.sidebar.checkbox("**Show Column Info**")
st.markdown("# Insurance Charges Exploration")
st.markdown("In a recent survey conducted by Gallup and West Health, an estimated 112 million Americans (44%) struggle to pay for [healthcare](https://www.westhealth.org/press-release/112-million-americans-struggle-to-afford-healthcare/#:~:text=WASHINGTON%2C%20D.C.%20%E2%80%94%20Mar.,is%20not%20worth%20the%20cost)."
            " National health spending is over 4 trillion in this country, and current projections indicate it will continue to grow at an annual rate of 5.4%, topping $6.2 trillion by 2028. "
            "Furthermore, [The Wall Street Journal](https://www.wsj.com/health/healthcare/health-insurance-cost-increase-5b35ead7) has recently reported that insurance rates are set to increase more than the projected rate, at 6.5%. This would mark on of the biggest price increase in years. "
            )
st.write(" The goal of this application is to provide visualizations to the user to help determine factors contributing to their insurance costs."
        " At a future date the goal is too allow the user to input information about themselves and determine factors that impact their insurance rate."
            " **Please note that there are several factors that this dataset does not include that may contribute to the cost of insurance.** ")
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
Dist= st.sidebar.checkbox('**Data and Distribution**')
if Dist:
    st.markdown(" ## The Insurance Dataset")
    st.write("*This dataset contains information and statistics related to health insurance costs in the United States. For a more detailed description of the dataset, please refer to the sidebar.*")
    data_preview = st.checkbox("View Data Table")
    if data_preview:
        st.write("### Dataset Preview")
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

    st.markdown("## Distribution of each variable")
    st.write("The dataset contains several variables that may contribute to the cost of insurance for an individual. As a way to quickly observe the number of observationss for each variable, distributions may be plotted below:")


    # Basic Dists 

    show_age = st.checkbox("Age")
    show_children =st.checkbox("Children")
    show_sex =st.checkbox("Gender")
    show_bmi =st.checkbox("BMI")
    show_smoker =st.checkbox("Smoker")
    show_region =st.checkbox("Region")




    if show_age:
        fig = px.histogram(insurance, x='age', marginal='box', nbins=100, title='Distribution of Age', color = 'age')
        fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)
        st.write("*We see that while there are individuals from all ages in the dataset, a larger number of 18 and 19 year olds than another other age. Let's keep this in mind when we think of other data.*")

    if show_children:
        fig = px.histogram(insurance, x='children', marginal='box', nbins=64, title='Distribution of Children', color ='children')
        fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)
        st.write("*The most common amount of children in the dataset are that of zero. Also, we can see the overall distribution of the data is heavily right skewed.*")

    if show_sex:
        fig = px.histogram(insurance, x='sex',  nbins=64, title='Distribution of Gender',color ='sex')
        fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)
        st.write("*The proportion of males to females are very close. There are only 14 more males than females in the data.*")

    if show_bmi:
        fig = px.histogram(insurance, x='bmi', marginal='box', nbins=64, title='Distribution of BMI')
        fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)
        st.write("*The distribution of BMI is nearly guassian, which is to be expected in nature.*")
    if show_smoker:
        fig = px.histogram(insurance, x='smoker', marginal='box', nbins=64, title='Distribution of Smokers',color = 'smoker')
        fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)
        st.write("*There are fare greater non-smokers than smokers.*")
    if show_region:
        fig = px.histogram(insurance, x='region', nbins=64, title='Distribution of Region',color = 'region')
        fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
        st.plotly_chart(fig, use_container_width=True)
        st.write("*The number of people in each region are close.*")

Dist2= st.sidebar.checkbox('**Relationships**')
if Dist2:
    df = df1
    cols = df.columns
    st.markdown("### Now that we know what the distributions of each variable are, we can investigate several relationships in the data ")
    st.write("Although distributions might tell us some basic information about the data, we can gain more information by creating plots of the relationship between the variables.")
    st.write("**Please select variables that you wish to plot.** *If two numeric values are selected, use a scatter plot. If only one, use a bar chart.*")
    x_val = st.selectbox('Variable on the x-axis?', cols)
    y_val = st.selectbox('Variable on the y-axis?', cols)
    z_val = st.selectbox('Do you want a hue?', cols)

    button3 = st.button("Bar Chart")
    if button3:
        st.write(f"Mean {y_val} by {x_val}")
        mean_data = df.groupby(x_val)[y_val].mean().reset_index()
        fig = px.bar(mean_data, x=x_val, y=y_val,color=x_val)
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

    st.markdown("### Our next goal is to investigate serveral factors that might contribute to the prices of insurance for individuals ")
    st.write("Let's start with a view of the distribution of charges:")


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
    st.write("*The number of children do not really give us information on the charges, we can see that the data is close. Do note there are several outliers in the data.*")
    st.markdown("### Is region a contributing factor?")
    boxplot_fig = px.violin(insurance, x='region', y='charges',color='region', title='Insurance Charges by Region')
    boxplot_fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
    st.plotly_chart(boxplot_fig, use_container_width=True)
    st.write("*The charges by region are not indicative of high or low rates of insurance charges.*")

    st.markdown("### Does Sex impact cost?")
    boxplot_fig = px.box(insurance, x='sex', y='charges',color='sex', title='Insurance Charges by Sex')
    boxplot_fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
    st.plotly_chart(boxplot_fig, use_container_width=True)
    mean_databar = insurance.groupby('sex')['charges'].mean().reset_index()
    bbarplot_fig = px.bar(mean_databar, x='sex', y='charges',color='sex', title='Insurance Charges by Sex')
    bbarplot_fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
    st.plotly_chart(bbarplot_fig, use_container_width=True)
    st.write("*The distribution of charges for males are slightly higher than that of females. The mean insurance charge for males is roughly 14,000 dollars. For females, we see the mean is roughly 12,500 dollars. Interesting, the females have a slightly higher median charge than males.*")
    



    st.markdown("### Let's investigate the relationship if BMI and Age to the Charges.")
  

    scatter_fig = px.scatter(insurance, x='age', y='charges')
    scatter_fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
    st.plotly_chart(scatter_fig, use_container_width=True)

    scatter_fig = px.scatter(insurance, x='bmi', y='charges')
    scatter_fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
    st.plotly_chart(scatter_fig, use_container_width=True)
    st.write("*These plots are both intersting, we don't see a glaring relationship, but we also observe there is almost two lines in both data. These two lines seem to seperate as well.*")
    st.markdown("### Try adding the 'smoker' hue")
    hue_for = st.checkbox("**Add Smoker hue to the dataset**")
    if hue_for:
            scatter_figage = px.scatter(insurance, x='age', y='charges',color ='smoker')
            scatter_figage.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
            st.plotly_chart(scatter_figage, use_container_width=True)
            scatter_figbmi = px.scatter(insurance, x='bmi', y='charges',color ='smoker')
            scatter_figbmi.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
            st.plotly_chart(scatter_figbmi, use_container_width=True)



    st.markdown(" ## The culprit seams to be determined by if one is a smoker or not!")

    st.write("***So, how many smokers are there in the dataset?***" )

    fig = px.histogram(insurance, x='smoker', nbins=64, title='Distribution of Smokers', color='smoker')
    fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)

    st.write(f"**Mean {'charges'} by {'smoker'}**")
    mean_data3 = df.groupby('smoker')['charges'].mean().reset_index()
    fig = px.bar(mean_data3, x='smoker', y='charges',color='smoker')
    st.plotly_chart(fig, use_container_width=True)



    st.markdown('### So, what is next')
    with st.expander(  "# Click here to see!"):
        st.write("The next step is to create a regression model based on the parameters in this dataset to help determine and predict charges for individuals!. ")


hipl= st.sidebar.checkbox("**Hiplot**")
if hipl:
    st.markdown(" ## Hiplot Visualization")


    st.write('**This tab shows a Hiplot of the data. With this plot, the user is able to fine tune the plot to their specific interests**')

    exp = hip.Experiment.from_dataframe(insurance)
    htmlcomp=exp.to_html()
    st.components.v1.html(htmlcomp,width=900, height=600, scrolling=True)
nxt = st.sidebar.checkbox("**Next Steps**")
if nxt:
    st.markdown('### So, what is next?')
    with st.expander(  "# Click here to see!"):
        st.write("The next step is to create a regression model based on the parameters in this dataset to help determine and predict charges for individuals!")