import streamlit as st
st.set_page_config(layout="wide", page_title="Dashboard Audit Team", page_icon="📊")

from my_pages import page1, page2, page3, page4, page5, page6
from user_data import users, user_permissions
from datetime import datetime
from log_utils import log_event
from streamlit_javascript import st_javascript
import csv

# -----------------------------
# Mapping หน้า
# -----------------------------
page_mapping = {
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
    "Page 5": page5,
    "Page 6": page6
}

# -----------------------------
# ธีม AIS + Bootstrap
# -----------------------------
def set_ais_theme():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter&family=Prompt&display=swap" rel="stylesheet">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">

    <style>
    body, .stApp {
        background-color: #ffffff;
        color: #333333;
        font-family: 'Inter', 'Prompt', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        font-size: 16px;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #78BE20;
        font-weight: 600;
        line-height: 1.4;
        letter-spacing: 0.5px;
    }

    .btn-success {
        background-color: #78BE20 !important;
        border-color: #78BE20 !important;
    }
    .btn-success:hover {
        background-color: #66a81a !important;
        border-color: #66a81a !important;
    }

    .stButton>button {
        background-color: #78BE20;
        color: white !important;
        font-weight: bold;
        border: none;
        border-radius: 6px;
        padding: 0.5em 1.2em;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #66a81a;
        transform: scale(1.02);
    }

    .block-container {
        padding-top: 0.5rem !important;
    }

    header[data-testid="stHeader"] {
        background-color: #00573D;
        color: white;
    }

    header[data-testid="stHeader"] .st-emotion-cache-18ni7ap {
        color: white !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            header[data-testid="stHeader"] {
                background-color: #00573D;
                color: white;
            }
            header[data-testid="stHeader"] .st-emotion-cache-18ni7ap {
                color: white !important;
                font-weight: bold;
            }
            .block-container {
                padding-top: 1rem !important;
            }
        </style>
    """, unsafe_allow_html=True)

# -----------------------------
# ฟังก์ชัน Login
# -----------------------------
def login():
    set_ais_theme()

    st.markdown("""
        <div style='
            text-align: center; 
            font-size: 40px; 
            font-weight: bold; 
            padding-top: 1rem;
            margin-bottom: -6rem;
            line-height: 4;
            background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); 
            -webkit-background-clip: text;
            color: transparent;
        '>
            🔐 Audit Team Dashboard
        </div>
    """, unsafe_allow_html=True)

    user_agent = st_javascript(code="navigator.userAgent", key="ua_login") or "Unknown"
    ip = st_javascript(code="await fetch('https://api.ipify.org?format=json').then(res => res.json()).then(data => data.ip)", key="ip_login") or "Unknown"

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            st.markdown("## 👤 เข้าสู่ระบบผู้ใช้")
            username = st.text_input("👤 Username")
            password = st.text_input("🔑 Password", type="password")
            submitted = st.form_submit_button("🚪 เข้าสู่ระบบ")

            if submitted:
                user = users.get(username)
                if user and user["password"] == password:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.fullname = user["fullname"]
                    st.session_state.position = user["position"]
                    st.session_state.department = user["department"]
                    st.session_state.profile_pic = user.get("profile_pic", f"https://i.pravatar.cc/150?u={username}")

                    log_event(username, user["fullname"], browser=user_agent, page="Login", event="login", ip=ip)

                    with open('user_login_log.csv', mode='a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow([datetime.now(), username, user['fullname'], ip, user_agent])

                    st.success(f"🎉 ยินดีต้อนรับคุณ {user['fullname']}")
                    st.rerun()
                else:
                    st.error("❌ Username หรือ Password ไม่ถูกต้อง")

# -----------------------------
# หน้า Main App
# -----------------------------
def main_app():
    set_ais_theme()
    username = st.session_state.username
    fullname = st.session_state.fullname
    allowed_pages = user_permissions.get(username, [])

    display_name_map = {
        "HOME": "Page 1",
        "Page 2": "Page 2",
        "Page 3": "Page 3",
        "Page 4": "Page 4",
        "Page 5": "Page 5",
        "Page 6": "Page 6"
    }

    display_options = [display for display, real in display_name_map.items() if real in allowed_pages]
    selected_display = st.sidebar.selectbox("📁 เลือกหน้า", display_options)
    page = display_name_map[selected_display]

    with st.sidebar:
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        st.image(st.session_state.profile_pic, width=100)
        st.markdown("</div>", unsafe_allow_html=True)
    st.sidebar.markdown(f"**👤 {fullname}**")
    st.sidebar.markdown(f"💼 {st.session_state.position}")
    st.sidebar.markdown(f"🏢 {st.session_state.department}")
    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 ออกจากระบบ"):
        for key in ["logged_in", "username", "fullname", "position", "department", "profile_pic"]:
            st.session_state.pop(key, None)
        st.rerun()

    user_agent = st_javascript(code="navigator.userAgent", key="ua_main") or "Unknown"
    ip = st_javascript(code="await fetch('https://api.ipify.org?format=json').then(res => res.json()).then(data => data.ip)", key="ip_main") or "Unknown"
    log_event(username, fullname, browser=user_agent, page=page, event="visit_page", ip=ip)

    st.markdown(f"<h2 class='text-success'>📄 {selected_display}</h2>", unsafe_allow_html=True)
    if page in page_mapping:
        page_mapping[page].show()

# -----------------------------
# Main
# -----------------------------
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        main_app()
    else:
        login()

if __name__ == "__main__":
    main()
