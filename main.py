import os
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st


# set page configuration
st.set_page_config(page_title = "Data Visualiser",
                   layout='centered',
                   page_icon='📊')

# title
st.title('📊 Data Visuliser - Web App')

# getting the working directory of main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dir}/data"

# List the files present in "data" folder
files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Dropdown for all the files 
selected_files = st.selectbox("Select a file", files, index=None)

if selected_files:
    # get the complete path of the selected file

    file_path = os.path.join(folder_path,selected_files)

    # reading the csv files as a pandas dataframe
    df = pd.read_csv(file_path)

    col1,col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())  

    with col2:
        # user selection of df columns

        x_axis = st.selectbox("Select the X-axis", options=columns+['None'],index = None)
        y_axis = st.selectbox("Select the y-axis", options=columns+['None'],index=None)              

        plot_list = ['Line Plot','Bar Chart','Scatter Plot','Distribution Plot','Count Plot']

        selected_plot = st.selectbox('Select a Plot',options=plot_list,index=None)

        # st.write(x_axis)
        # st.write(y_axis)
        # st.write(selected_plot)


    # button to generate plots
    if st.button("Generate Plot"):
        fig,ax = plt.subplots(figsize=(6,4)) 

        if selected_plot == "Line Plot":
            sns.lineplot(x=df[x_axis],y=df[y_axis],ax=ax)    

        elif selected_plot == "Bar Chart":
            sns.barplot(x=df[x_axis],y=df[y_axis],ax=ax) 

        elif selected_plot == "Scatter Plot":
            sns.scatterplot(x=df[x_axis],y=df[y_axis],ax=ax) 

        elif selected_plot == "Distribution Plot":
            sns.histplot(df[x_axis],kde=True,ax=ax)   

        elif selected_plot == "Count Plot":
            sns.histplot(x=df[x_axis],ax=ax)  


        # adjust label sizes
        ax.tick_params(axis='x',labelsize=10)           
        ax.tick_params(axis='y',labelsize=10)  

        # title axes labels
        plt.title(f"{selected_plot} of {y_axis} vs {x_axis}",fontsize=12)
        plt.xlabel(x_axis,fontsize=10)         
        plt.ylabel(y_axis,fontsize=10)   

        st.pyplot(fig)      
          
