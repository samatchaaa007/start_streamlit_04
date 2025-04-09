import streamlit as st
import pandas as pd
import time

# ---------------------------
# CSS Styling สำหรับ Block
# ---------------------------
st.markdown("""
    <style>
    .block {
        border: 2px solid #d9d9d9;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.05);
    }
    .block h2 {
        color: #1a3e5f;
        margin-bottom: 10px;
    }
    .block h3 {
        color: #3c3c3c;
        margin-top: 0;
    }
    </style>
""", unsafe_allow_html=True)


def show():
    # ----------------------
    # Header Block
    # ----------------------
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("## 🚀 ยินดีต้อนรับสู่ Dashboard ของเรา", unsafe_allow_html=True)
    st.markdown("""
    ### เกี่ยวกับระบบ  
    ระบบนี้ถูกออกแบบมาเพื่อแสดงข้อมูล Redeem, ประมวลผลข้อมูล, และแสดงผลในรูปแบบ Interactive Dashboard อย่างมืออาชีพ ✨  
    คุณสามารถดูภาพรวมข้อมูล, วิเคราะห์เชิงลึก, หรือกรองข้อมูลผ่าน Sidebar ได้ทันที
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ----------------------
    # Loading Block
    # ----------------------
    with st.spinner("กำลังโหลดข้อมูลเบื้องต้น..."):
        time.sleep(1.5)
    st.success("โหลดข้อมูลสำเร็จแล้ว! ✅")

    # ----------------------
    # Code Example Block
    # ----------------------
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("## 🔧 ตัวอย่างการเขียนโค้ด Python", unsafe_allow_html=True)
    st.markdown("ลองกดปุ่มเพื่อดูตัวอย่างโค้ด", unsafe_allow_html=True)
    code = '''
def hello():
    print("Hello, Streamlit!")'''
    with st.expander("📜 แสดงตัวอย่างโค้ด"):
        st.code(code, language='python')
    st.markdown('</div>', unsafe_allow_html=True)

    # ----------------------
    # Input Block
    # ----------------------
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("## 🧪 ทดลองป้อนข้อมูล", unsafe_allow_html=True)
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
    # Chart Block
    # ----------------------
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.markdown("## 📈 แสดงตัวอย่างกราฟแบบเส้น", unsafe_allow_html=True)
    df = pd.DataFrame({
        'x': list(range(10)),
        'y': [x**2 for x in range(10)]
    })
    st.line_chart(df, x='x', y='y')
    st.markdown('</div>', unsafe_allow_html=True)

# เรียกใช้
show()
