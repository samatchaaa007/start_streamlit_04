import streamlit as st
import pandas as pd
import time

#st.set_page_config(layout="wide")

def show():
    # ----------------------
    # Header
    # ----------------------
    st.title("🚀 ยินดีต้อนรับสู่ Dashboard ของเรา")
    st.markdown("""
    ### เกี่ยวกับระบบ
    ระบบนี้ถูกออกแบบมาเพื่อแสดงข้อมูล Redeem, ประมวลผลข้อมูล, และแสดงผลในรูปแบบ Interactive Dashboard อย่างมืออาชีพ ✨

    คุณสามารถดูภาพรวมข้อมูล, วิเคราะห์เชิงลึก, หรือกรองข้อมูลผ่าน Sidebar ได้ทันที
    """)

    # ----------------------
    # Animation Spinner
    # ----------------------
    with st.spinner("กำลังโหลดข้อมูลเบื้องต้น..."):
        time.sleep(1.5)
    st.success("โหลดข้อมูลสำเร็จแล้ว! ✅")

    # ----------------------
    # Code Example with st.echo
    # ----------------------
    st.markdown("""
    ## 🔧 ตัวอย่างการเขียนโค้ด Python
    ลองกดปุ่มเพื่อดูตัวอย่างโค้ด
    """)

    code = '''
def hello():
    print("Hello, Streamlit!")'''

    with st.expander("📜 แสดงตัวอย่างโค้ด"):
        st.code(code, language='python')

    # ----------------------
    # Columns for user input
    # ----------------------
    st.markdown("---")
    st.markdown("## 🧪 ทดลองป้อนข้อมูล")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("กรอกอายุของคุณ", min_value=0, max_value=120)
        st.info(f"คุณอายุ {age} ปี")

    with col2:
        text = st.text_input("พิมพ์ข้อความอะไรก็ได้")
        if text:
            tokens = text.split()
            st.success(f"Tokenized: {' | '.join(tokens)}")

    # ----------------------
    # Sample Chart
    # ----------------------
    st.markdown("---")
    st.markdown("## 📈 แสดงตัวอย่างกราฟแบบเส้น")

    df = pd.DataFrame({
        'x': list(range(10)),
        'y': [x**2 for x in range(10)]
    })

    st.line_chart(df, x='x', y='y')

# เรียกใช้
show()
