import streamlit as st
import pandas as pd
import time

# Custom CSS
st.markdown("""
    <style>
    .block {
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .block h2, .block h3 {
        color: #2c3e50;
        margin-top: 0;
    }
    </style>
""", unsafe_allow_html=True)

def show():
    # ----------------------
    # Header
    # ----------------------
    st.markdown('<div class="block"><h2>🚀 ยินดีต้อนรับสู่ Dashboard ของเรา</h2>' +
                '<h3>เกี่ยวกับระบบ</h3>' +
                'ระบบนี้ถูกออกแบบมาเพื่อแสดงข้อมูล Redeem, ประมวลผลข้อมูล, และแสดงผลในรูปแบบ Interactive Dashboard อย่างมืออาชีพ ✨<br>' +
                'คุณสามารถดูภาพรวมข้อมูล, วิเคราะห์เชิงลึก, หรือกรองข้อมูลผ่าน Sidebar ได้ทันที</div>', unsafe_allow_html=True)

    # ----------------------
    # Animation Spinner
    # ----------------------
    with st.spinner("กำลังโหลดข้อมูลเบื้องต้น..."):
        time.sleep(1.5)
    st.success("โหลดข้อมูลสำเร็จแล้ว! ✅")

    # ----------------------
    # Code Example
    # ----------------------
    st.markdown('<div class="block"><h3>🔧 ตัวอย่างการเขียนโค้ด Python</h3>' +
                'ลองกดปุ่มเพื่อดูตัวอย่างโค้ด</div>', unsafe_allow_html=True)

    code = '''
def hello():
    print("Hello, Streamlit!")'''

    with st.expander("📜 แสดงตัวอย่างโค้ด"):
        st.code(code, language='python')

    # ----------------------
    # User Input
    # ----------------------
    st.markdown('<div class="block"><h3>🧪 ทดลองป้อนข้อมูล</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("กรอกอายุของคุณ", min_value=0, max_value=120)
        st.info(f"คุณอายุ {age} ปี")
    with col2:
        text = st.text_input("พิมพ์ข้อความอะไรก็ได้")
        if text:
            tokens = text.split()
            st.success(f"Tokenized: {' | '.join(tokens)}")

    st.markdown('</div>', unsafe_allow_html=True)

    # ----------------------
    # Chart
    # ----------------------
    st.markdown('<div class="block"><h3>📈 แสดงตัวอย่างกราฟแบบเส้น</h3>', unsafe_allow_html=True)

    df = pd.DataFrame({
        'x': list(range(10)),
        'y': [x**2 for x in range(10)]
    })
    st.line_chart(df, x='x', y='y')

    st.markdown('</div>', unsafe_allow_html=True)

# เรียกใช้
show()
