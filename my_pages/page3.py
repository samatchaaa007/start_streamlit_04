import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import numpy as np

#st.set_page_config(layout="wide")

def title():
    st.markdown("""
        <style>
            h1 {
                font-size: 20px;
                color: #78BE20;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

def show():
    title()
    st.h1("📈 Dashboard หน้า 3: วิเคราะห์ยอดขายเชิงลึก")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Summary Table", "📉 Line Chart", "📌 KPI Dashboard", "📎 Heatmap", "🧪 Interactive"
    ])

    # ---------------------------------------
    # ✅ ข้อมูลหลัก (ใช้ร่วมกันทุก Tab)
    # ---------------------------------------
    df_main = pd.DataFrame({
        "เดือน": ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย."],
        "ยอดขาย (บาท)": [120000, 135000, 99000, 150000, 170000, 160000],
        "จำนวนลูกค้า": [300, 340, 280, 360, 390, 370],
        "ความพึงพอใจ (%)": [85, 88, 82, 91, 93, 92]
    })

    df_main["เดือนที่"] = pd.date_range(start="2024-01-01", periods=6, freq='M')

    # ---------------------------------------
    with tab1:
        st.subheader("📊 รายงานสรุปยอดขาย")

        st.dataframe(
            df_main.style.format({
                "ยอดขาย (บาท)": "{:,.0f}",
                "จำนวนลูกค้า": "{:,.0f}",
                "ความพึงพอใจ (%)": "{:,.0f}"
            }).highlight_max(axis=0, color='lightgreen'),
            use_container_width=True
        )

        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(df_main, x="เดือน", y="ยอดขาย (บาท)", text="ยอดขาย (บาท)",
                         color="เดือน", title="ยอดขายรายเดือน",
                         color_discrete_sequence=px.colors.qualitative.Set3)
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = px.pie(df_main, names="เดือน", values="จำนวนลูกค้า",
                         title="สัดส่วนจำนวนลูกค้าแต่ละเดือน", hole=0.4)
            st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------------
    with tab2:
        st.subheader("📉 แนวโน้มยอดขายและความพึงพอใจ")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_main["เดือนที่"], y=df_main["ยอดขาย (บาท)"],
                                 mode='lines+markers', name='ยอดขาย'))
        fig.add_trace(go.Scatter(x=df_main["เดือนที่"], y=df_main["ความพึงพอใจ (%)"] * 1000,
                                 mode='lines+markers', name='ความพึงพอใจ (x1000)', yaxis='y2'))

        fig.update_layout(
            title="แนวโน้มยอดขายและความพึงพอใจ",
            xaxis_title="เดือน",
            yaxis=dict(title='ยอดขาย'),
            yaxis2=dict(title='ความพึงพอใจ', overlaying='y', side='right'),
            title_x=0.5
        )
        st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------------
    with tab3:
        st.subheader("📌 KPI Dashboard")

        total_sales = df_main["ยอดขาย (บาท)"].sum()
        new_customers = df_main["จำนวนลูกค้า"].sum()
        avg_satisfaction = df_main["ความพึงพอใจ (%)"].mean()

        col1, col2, col3 = st.columns(3)

        def kpi_card(col, value, label, color):
            col.metric(label=label, value=f"{value:,.0f}")
            col.markdown(f"<div style='height:5px;background-color:{color};border-radius:4px;'></div>", unsafe_allow_html=True)

        kpi_card(col1, total_sales, "ยอดขายรวม", "#4CAF50")
        kpi_card(col2, new_customers, "ลูกค้าทั้งหมด", "#2196F3")
        kpi_card(col3, avg_satisfaction, "ความพึงพอใจเฉลี่ย (%)", "#FFC107")

        st.markdown("---")
        st.markdown("### 🎯 วิเคราะห์ความพึงพอใจ")
        st.bar_chart(df_main.set_index("เดือน")["ความพึงพอใจ (%)"])

    # ---------------------------------------
    with tab4:
        st.subheader("📎 Heatmap: ยอดขายรายวัน")

        days = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        weeks = ["สัปดาห์ที่ 1", "สัปดาห์ที่ 2", "สัปดาห์ที่ 3", "สัปดาห์ที่ 4"]
        z_data = np.random.randint(50, 200, size=(len(weeks), len(days)))

        fig = go.Figure(data=go.Heatmap(
            z=z_data,
            x=days,
            y=weeks,
            colorscale='YlGnBu'))

        fig.update_layout(title='Heatmap ยอดขายรายวันในแต่ละสัปดาห์', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------------
    with tab5:
        st.subheader("🧪 ตัวอย่างลูกเล่นพิเศษ")

        def stream_data():
            _LOREM_IPSUM = """
            Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
            incididunt ut labore et dolore magna aliqua.
            """
            for word in _LOREM_IPSUM.split():
                yield word + " "
                time.sleep(0.03)
            yield pd.DataFrame(np.random.randn(5, 10), columns=list("abcdefghij"))

        if st.button("เริ่ม Stream ข้อมูล!"):
            st.write_stream(stream_data)

# เรียกใช้งาน
show()
