import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import numpy as np


def show():
    st.write("### 📈 Dashboard หน้า 3")
    st.write("เน้นการแสดงข้อมูลเชิงลึกด้วย Table + Chart แบบสวยงาม ✨")

    tab1, tab2, tab3, tab4 ,tab5 = st.tabs([
        "📊 Summary Table", "📉 Line Chart", "📌 KPI Dashboard", "📎 Heatmap" , "Test"
    ])

    with tab1:
        st.subheader("📊 รายงานสรุปยอดขาย")
        data = {
            "เดือน": ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย."],
            "ยอดขาย (บาท)": [120000, 135000, 99000, 150000, 170000, 160000],
            "จำนวนลูกค้า": [300, 340, 280, 360, 390, 370]
        }
        df = pd.DataFrame(data)

        st.dataframe(
            df.style.format({
                "ยอดขาย (บาท)": "{:,.0f}",
                "จำนวนลูกค้า": "{:,.0f}"
            }).highlight_max(axis=0, color='lightgreen'),
            use_container_width=True
        )

        fig = px.bar(df, x="เดือน", y="ยอดขาย (บาท)", text="ยอดขาย (บาท)",
                     color="เดือน", title="ยอดขายรายเดือน",
                     color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("📉 แนวโน้มยอดขาย")
        df = pd.DataFrame({
            "เดือน": pd.date_range(start="2024-01-01", periods=6, freq='M'),
            "ยอดขาย": [120, 135, 99, 150, 170, 160]
        })

        fig = px.line(df, x="เดือน", y="ยอดขาย", markers=True,
                      title="แนวโน้มยอดขายรายเดือน")
        fig.update_layout(title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("📌 KPI Dashboard")

        col1, col2, col3 = st.columns(3)

        def kpi_card(col, value, label, color):
            col.metric(label=label, value=f"{value:,}", delta=None)
            col.markdown(f"<div style='height:5px;background-color:{color};border-radius:4px;'></div>", unsafe_allow_html=True)

        kpi_card(col1, 480000, "ยอดขายสะสม", "#4CAF50")
        kpi_card(col2, 2050, "จำนวนลูกค้าใหม่", "#2196F3")
        kpi_card(col3, 92, "ความพึงพอใจ (%)", "#FF9800")

    with tab4:
        st.subheader("📎 Heatmap: ยอดขายรายวัน")

        days = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        weeks = ["สัปดาห์ที่ 1", "สัปดาห์ที่ 2", "สัปดาห์ที่ 3", "สัปดาห์ที่ 4"]
        import numpy as np
        z_data = np.random.randint(50, 200, size=(len(weeks), len(days)))

        fig = go.Figure(data=go.Heatmap(
            z=z_data,
            x=days,
            y=weeks,
            colorscale='YlGnBu'))

        fig.update_layout(title='Heatmap ยอดขายรายวันในแต่ละสัปดาห์', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)

    with tab5 :
        

        _LOREM_IPSUM = """
        Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
        nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        """
        _LOREM_IPSUM2 = "CHAEIEIEIEIEIEIEIEIEIEIEI"

        def stream_data():
            for word in _LOREM_IPSUM.split(" "):
                yield word + " "
                time.sleep(0.02)

            yield pd.DataFrame(
                np.random.randn(5, 10),
                columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
            )

            for word in _LOREM_IPSUM2.split(" "):
                yield word + " "
                time.sleep(0.02)


        if st.button("Stream data"):
            st.write_stream(stream_data)