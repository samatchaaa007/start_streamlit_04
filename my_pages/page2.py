import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ✅ ต้องอยู่บรรทัดแรกสุด
# st.set_page_config(layout="wide")

def show():
    st.title("📊 Dashboard รวมข้อมูล Redeem")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Overview", "📦 Stacked Bar", "🔵 Bubble Chart", "🌞 Pie & Sunburst", "📋 Data Table"
    ])

    # ------------------------------
    # ✅ กำหนดข้อมูลหลัก
    # ------------------------------
    data = {
        "Category": ["A", "B", "C", "D", "E", "F", "G", "H"],
        "Value": [100, 200, 150, 300, 250, 356, 789, 670],
        "Region": ["North", "South", "East", "West", "North", "East", "West", "North"],
        "Quarter": ["Q1", "Q2", "Q3", "Q1", "Q2", "Q3", "Q4", "Q4"],
        "Type": ["Type1", "Type2", "Type1", "Type3", "Type1", "Type2", "Type3", "Type2"]
    }

    df = pd.DataFrame(data)

    # ------------------------------
    # ✅ Sidebar Filters
    # ------------------------------
    with st.sidebar:
        st.header("🔎 ตัวกรองข้อมูล")

        filter_region = st.multiselect("🌍 เลือก Region", df["Region"].unique(), default=df["Region"].unique())
        filter_category = st.multiselect("📦 เลือก Category", df["Category"].unique(), default=df["Category"].unique())
        filter_type = st.multiselect("🧩 เลือก Type", df["Type"].unique(), default=df["Type"].unique())
        value_min, value_max = st.slider("💰 เลือกช่วง Value", min_value=int(df["Value"].min()), 
                                        max_value=int(df["Value"].max()), 
                                        value=(int(df["Value"].min()), int(df["Value"].max())))

    df_filtered = df[
        df["Region"].isin(filter_region) &
        df["Category"].isin(filter_category) &
        df["Type"].isin(filter_type) &
        df["Value"].between(value_min, value_max)
    ]

    def create_card(col, value, title, bg_color, text_color, shadow_color):
        col.markdown(
            f"""
            <div style="
                background-color: {bg_color}; 
                padding: 20px; 
                border-radius: 15px; 
                text-align: center;
                height: 150px; 
                display: flex; 
                flex-direction: column; 
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                font-weight: bold;
                box-shadow: 4px 4px 10px {shadow_color};
            ">
                <h1 style="color: {text_color}; font-size: 36px; margin-bottom: 5px;">{value:,}</h1>
                <h3 style="color: #333; font-size: 20px;">{title}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ------------------------------
    # 🏠 Tab 1: Overview
    # ------------------------------
    with tab1:
        st.subheader("ภาพรวมตาม Region")
        df_region_sum = df_filtered.groupby("Region")["Value"].sum().reset_index()

        north_total = df_region_sum[df_region_sum["Region"] == "North"]["Value"].sum()
        south_total = df_region_sum[df_region_sum["Region"] == "South"]["Value"].sum()
        east_total = df_region_sum[df_region_sum["Region"] == "East"]["Value"].sum()
        west_total = df_region_sum[df_region_sum["Region"] == "West"]["Value"].sum()

        col1, col2, col3, col4 = st.columns(4)
        create_card(col1, north_total, "North", "#FFCDD2", "#B71C1C", "rgba(183,28,28,0.2)")
        create_card(col2, south_total, "South", "#C8E6C9", "#1B5E20", "rgba(27,94,32,0.2)")
        create_card(col3, east_total, "East", "#BBDEFB", "#0D47A1", "rgba(13,71,161,0.2)")
        create_card(col4, west_total, "West", "#FFF9C4", "#FF6F00", "rgba(255,111,0,0.2)")

        st.plotly_chart(px.bar(df_region_sum, x="Region", y="Value", color="Region", 
                               title="Bar Chart by Region"))

    # ------------------------------
    # 📦 Tab 2: Stacked Bar
    # ------------------------------
    with tab2:
        st.subheader("Stacked Bar Chart แสดงหมวดหมู่")
        stacked_df = df_filtered.groupby(["Region", "Category"])["Value"].sum().reset_index()
        fig = px.bar(stacked_df, x="Category", y="Value", color="Region", barmode='stack',
                     title="Stacked Bar Chart")
        st.plotly_chart(fig)

    # ------------------------------
    # 🔵 Tab 3: Bubble Chart
    # ------------------------------
    with tab3:
        st.subheader("Bubble Chart แสดงขนาดตาม Value")
        df_filtered["Size"] = df_filtered["Value"] * 5
        fig = px.scatter(df_filtered, x="Category", y="Value", size="Size", color="Region",
                         hover_name="Category", title="Bubble Chart")
        st.plotly_chart(fig)

    # ------------------------------
    # 🌞 Tab 4: Pie & Sunburst
    # ------------------------------
    with tab4:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Pie Chart")
            pie_df = df_filtered.groupby("Region")["Value"].sum().reset_index()
            fig = px.pie(pie_df, names="Region", values="Value", hole=0.4)
            st.plotly_chart(fig)
        with col2:
            st.subheader("Sunburst Chart")
            if len(df_filtered) > 0:
                fig = px.sunburst(df_filtered, path=["Region", "Type", "Category"], values="Value")
                st.plotly_chart(fig)
            else:
                st.info("No data available for Sunburst Chart")

    # ------------------------------
    # 📋 Tab 5: Data Table
    # ------------------------------
    with tab5:
        st.subheader("ตารางข้อมูลหลังการกรอง")
        st.dataframe(df_filtered.style.format({"Value": "{:,.0f}"}), use_container_width=True)

# เรียกใช้งาน show()
show()
