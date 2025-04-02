import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="View Dashboard", layout="wide")

# --- โหลดข้อมูล ---
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

df = load_data()

st.markdown(
    """
    <style>
    /* เขียว สำหรับ multiselect แรก (เลือกวัน) */
    div[data-testid="stSidebar"] div:nth-child(2) .stMultiSelect > div {
        background-color: #2ecc71;
    }

    /* น้ำเงิน สำหรับ multiselect ที่สอง (เลือกเพศ) */
    div[data-testid="stSidebar"] div:nth-child(3) .stMultiSelect > div {
        background-color: #3498db;
    }

    /* ปรับสีตัวหนังสือบนปุ่มให้ contrast */
    .stMultiSelect div[role="option"] {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- UI Sidebar ---
st.sidebar.header("Filter")
selected_day = st.sidebar.multiselect("เลือกวัน:", options=df['day'].unique(), default=df['day'].unique())
selected_sex = st.sidebar.multiselect("เลือกเพศ:", options=df['sex'].unique(), default=df['sex'].unique())

# --- Filtered Data ---
filtered_df = df[(df['day'].isin(selected_day)) & (df['sex'].isin(selected_sex))]

# --- Header + Stats ---
st.title("👁️‍🗨️ View ข้อมูลร้านอาหาร")
col1, col2, col3 = st.columns(3)
col1.metric("จำนวนรายการ", len(filtered_df))
col2.metric("ทิปเฉลี่ย 💵", f"${filtered_df['tip'].mean():.2f}")
col3.metric("รวมยอดขาย 💰", f"${filtered_df['total_bill'].sum():.2f}")

# --- ตารางข้อมูล + กราฟ ---
st.subheader("📋 ตารางข้อมูล")
st.dataframe(filtered_df, use_container_width=True)

fig = px.bar(filtered_df.groupby('day')['tip'].mean().reset_index(), x='day', y='tip')
st.plotly_chart(fig, use_container_width=True)
