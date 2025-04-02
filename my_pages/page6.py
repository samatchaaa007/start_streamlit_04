import streamlit as st
import pandas as pd
import os

def show():
    st.title("📜 Log Viewer")

    log_path = "user_login_log.csv"

    if os.path.exists(log_path):
        try:
            # ✅ ใช้ on_bad_lines='skip' เพื่อข้ามบรรทัดที่ไม่ตรงคอลัมน์
            df = pd.read_csv(log_path, on_bad_lines='skip')

            st.markdown("## 📂️ ข้อมูล Log ล่าสุด")
            st.dataframe(df.sort_values(by='timestamp', ascending=False), use_container_width=True)

            # ✅ แปลง timestamp ก่อนใช้
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

            if 'username' in df.columns:
                st.markdown("## 📊 จำนวนครั้งเข้าใช้งานต่อผู้ใช้")
                count_df = df['username'].value_counts().reset_index()
                count_df.columns = ['username', 'login_count']
                st.bar_chart(count_df.set_index('username'))

            if 'timestamp' in df.columns:
                st.markdown("## 📈 Timeline การเข้าใช้งานรายวัน")
                timeline = df.groupby(df['timestamp'].dt.date).count()['username']
                st.line_chart(timeline)

            if 'event' in df.columns:
                st.markdown("## 🔄 ประเภท Event ที่เกิดขึ้น")
                event_df = df['event'].value_counts().reset_index()
                event_df.columns = ['event', 'count']
                st.bar_chart(event_df.set_index('event'))

            if 'browser' in df.columns:
                st.markdown("## 🌐 Browser ที่ใช้")
                browser_df = df['browser'].value_counts().reset_index()
                browser_df.columns = ['browser', 'count']
                st.bar_chart(browser_df.set_index('browser'))

            if 'page' in df.columns:
                st.markdown("## 📄 จำนวนครั้งที่เข้าแต่ละหน้า")
                page_df = df['page'].value_counts().reset_index()
                page_df.columns = ['page', 'count']
                st.bar_chart(page_df.set_index('page'))

            if 'ip' in df.columns:
                st.markdown("## 🌍 IP Address ที่ใช้บ่อย")
                ip_df = df['ip'].value_counts().reset_index()
                ip_df.columns = ['ip', 'count']
                st.bar_chart(ip_df.set_index('ip'))

            st.markdown("## 📅 ดาวน์โหลดไฟล์ Log")
            st.download_button(
                label="📅 ดาวน์โหลดเป็น CSV",
                data=df.to_csv(index=False),
                file_name="user_login_log.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดในการอ่าน log: {e}")
    else:
        st.warning("⚠️ ยังไม่มี log ถูกบันทึกในระบบ")