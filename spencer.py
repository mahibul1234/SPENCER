import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
st.title("_SPENCER SALE DASHBORD_")
st.markdown("-----")
df=pd.read_csv("spnaser supermarkt.csv")
st.write(df.head(3))

df['Item_Weight'] = df['Item_Weight'].fillna(0)
df['Outlet_Size'] = df['Outlet_Size'].fillna(0)


# ----show total sale---
total_sales=round(df['Item_Outlet_Sales'].sum())


st.markdown("-----")


st.subheader("Total Sales:")
st.subheader(f"RS {total_sales:,}")


#___ create ssider bar----

st.sidebar.header('FILTER HERE')

Product=st.sidebar.multiselect("select the product:",
options=df['Item_Type'].unique(),
default= df['Item_Type'].unique()[:3])


st.sidebar.header('FILTER HERE')
Outlet_Type=st.sidebar.multiselect("select the outlet:",

options=df['Outlet_Type'].unique(),
default=df['Outlet_Type'].unique())
#-- join  two unit---

df_selection = df.query(
    "Item_Type == @Product  & Outlet_Type == @Outlet_Type"
)
st.markdown("-----")
# ----carete table ----

sale=df_selection['Item_Type'].value_counts()

total_sales=pd.pivot_table(df_selection, index='Item_Type', values='Item_Outlet_Sales',aggfunc='sum').sort_values(by='Item_Outlet_Sales')


total_sales_outlet=pd.pivot_table(df_selection, index='Outlet_Type', values='Item_Outlet_Sales',aggfunc='sum').sort_values(by='Item_Outlet_Sales')

col1, col2,col3=st.columns(3)
with col1:
    st.write(total_sales)
    with col2:
        st.write(total_sales_outlet)
        with col3:
            st.write(sale)

st.title("_TOTAL SALE PRODUCT IN OUTLET_") 
st.markdown("----")
total_sales=pd.pivot_table(df_selection, index='Item_Type', values='Item_Outlet_Sales',aggfunc='sum').sort_values(by='Item_Outlet_Sales')
fig = px.bar(total_sales, x='Item_Outlet_Sales', y=total_sales.index)
st.plotly_chart(fig,use_container_width=True)

#---createpie chart---
st.markdown("----")
total_sales=pd.pivot_table(df_selection, index='Item_Type', values='Item_Outlet_Sales',aggfunc='sum').reset_index()
fig1 = px.pie(total_sales, names= 'Item_Type', values='Item_Outlet_Sales')
st.plotly_chart(fig1,use_container_width=True)
st.markdown("----")

st.markdown("NOTE This webapp developer by mahibul1234@gmail.com")



#  --- next day work----





