import streamlit as st
import pandas as pd
import plotly.express as px


def show() :
    # ------------------------------
    # Sample Data
    # ------------------------------
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'] * 25,
        'Value': [10, 20, 30, 40] * 25,
        'Date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
        'Region': ['North', 'South', 'East', 'West'] * 25
    })
    data['Month'] = data['Date'].dt.strftime('%B')

    # ------------------------------
    # Sidebar Filters
    # ------------------------------
    st.sidebar.title("🔍 Filter Data")
    selected_region = st.sidebar.multiselect("Select Region", options=data['Region'].unique(), default=data['Region'].unique())
    date_range = st.sidebar.date_input("Select Date Range", [data['Date'].min(), data['Date'].max()])
    selected_months = st.sidebar.multiselect("Select Month", options=data['Month'].unique(), default=data['Month'].unique())

    # Apply filters
    filtered_data = data[
        (data['Region'].isin(selected_region)) &
        (data['Month'].isin(selected_months)) &
        (data['Date'] >= pd.to_datetime(date_range[0])) &
        (data['Date'] <= pd.to_datetime(date_range[1]))
    ]

    # ------------------------------
    # Main Dashboard
    # ------------------------------
    st.title("📊 Dashboard")
    st.markdown("กราฟและตาราง")

    # Tabs
    tabs = st.tabs(["📈 Overview", "📊 Charts", "📋 Tables"])

    # ------------------------------
    # Tab 1: Overview
    # ------------------------------
    with tabs[0]:
        st.subheader("📌 Summary Overview")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records", len(filtered_data))
        col2.metric("Average Value", round(filtered_data['Value'].mean(), 2))
        col3.metric("Max Value", filtered_data['Value'].max())

        st.markdown("---")

        st.subheader("📋 Data Table")
        st.dataframe(filtered_data.head(100), use_container_width=True)

        st.markdown("---")

        st.subheader("📊 Quick Insights")

        # 🎨 Custom Colors (โทนสดใส + เป็นมิตรตา)
        custom_colors = [
            '#FF4C61',  # แดงสด
            '#00D97E',  # เขียวมินต์
            '#FFC145',  # เหลืองมะนาว
            '#3AA8F0',  # ฟ้าสด
            '#C084FC',  # ม่วงสดใส
            '#FF6B00'   # ส้มแฟนซี
        ]

        col4, col5 = st.columns(2)

        with col4:
            cat_fig = px.bar(
                filtered_data,
                x='Category',
                y='Value',
                color='Category',
                title='Value by Category',
                color_discrete_sequence=custom_colors
            )
            st.plotly_chart(cat_fig, use_container_width=True)

        with col5:
            region_fig = px.pie(
                filtered_data,
                names='Region',
                values='Value',
                title='Share by Region',
                color_discrete_sequence=custom_colors
            )
            st.plotly_chart(region_fig, use_container_width=True)

        # Line Chart: Monthly Total by Category
        line_month = px.line(
            filtered_data.groupby(['Month', 'Category']).sum(numeric_only=True).reset_index(),
            x='Month',
            y='Value',
            color='Category',
            title='Monthly Total by Category',
            color_discrete_sequence=custom_colors
        )
        st.plotly_chart(line_month, use_container_width=True)

    # ------------------------------
    # Tab 2: Charts
    # ------------------------------
    with tabs[1]:
        st.subheader("📊 Visualizations")

        col1, col2 = st.columns(2)

        with col1:
            bar_fig = px.bar(filtered_data, x='Category', y='Value', color='Region', barmode='group')
            st.plotly_chart(bar_fig, use_container_width=True)

        with col2:
            pie_fig = px.pie(filtered_data, names='Region', values='Value', title='Value Distribution by Region')
            st.plotly_chart(pie_fig, use_container_width=True)

        line_fig = px.line(filtered_data.groupby('Date').sum(numeric_only=True).reset_index(), x='Date', y='Value', title='Total Value Over Time')
        st.plotly_chart(line_fig, use_container_width=True)

    # ------------------------------
    # Tab 3: Tables
    # ------------------------------
    with tabs[2]:
        st.subheader("📋 Raw Data Table")
        st.dataframe(filtered_data, use_container_width=True)

        st.subheader("📊 Pivot Table")
        pivot_df = filtered_data.pivot_table(index='Category', columns='Region', values='Value', aggfunc='sum', fill_value=0)
        st.dataframe(pivot_df, use_container_width=True)