import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show():
    # -------------------------------
    # ส่วนที่ 1: Markdown แบบตัวหนา ตัวเอียง
    # -------------------------------
    st.markdown("*Streamlit* is **really** ***cool***.")

    # -------------------------------
    # ส่วนที่ 2: ใช้สีสันในข้อความ
    # -------------------------------
    st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.
    ''')

    # -------------------------------
    # ส่วนที่ 3: Emoji ดอกไม้
    # -------------------------------
    st.markdown("Here's a bouquet &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    # -------------------------------
    # ส่วนที่ 4: อธิบาย soft return กับ hard return
    # -------------------------------
    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)

    # -------------------------------
    # ส่วนที่ 5: Markdown Editor แบบ Interactive
    # -------------------------------
    st.markdown("---")  # เส้นคั่น

    st.subheader("📝 ลองพิมพ์ Markdown ด้วยตัวเอง")
    md = st.text_area('พิมพ์ข้อความ Markdown ที่คุณต้องการ (ไม่ต้องใส่เครื่องหมาย quote)',
                    "Happy Streamlit-ing! :balloon:")

    # แสดงตัวอย่างโค้ดที่ระบบจะใช้รัน
    st.code(f"""
    import streamlit as st

    st.markdown('''{md}''')
    """, language='python')

    # แสดงผลลัพธ์จริงของ markdown ที่ผู้ใช้พิมพ์
    st.markdown("### ผลลัพธ์:")
    st.markdown(md)

    st.caption("This is a string that explains something above.")
    st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
    st.write("This is some text.")

    st.slider("This is a slider", 0, 100, (25, 75))

    st.divider()  # 👈 Draws a horizontal rule

    st.write("This text is between the horizontal rules.")

    st.divider()  # 👈 Another horizontal rule

    def get_user_name():
        return 'John'

        with st.echo():
            # Everything inside this block will be both printed to the screen
            # and executed.

            def get_punctuation():
                return '!!!'

            greeting = "Hi there, "
            value = get_user_name()
            punctuation = get_punctuation()

            st.write(greeting, value, punctuation)

        # And now we're back to _not_ printing to the screen
        foo = 'bar'
        st.write('Done!')

    df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df = st.data_editor(
        df,
        column_config={
            "command": "Streamlit Command",
            "rating": st.column_config.NumberColumn(
                "Your rating",
                help="How much do you like this command (1-5)?",
                min_value=1,
                max_value=5,
                step=1,
                format="%d ⭐",
            ),
            "is_widget": "Widget ?",
        },
        disabled=["command", "is_widget"],
        hide_index=True,
    )

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


    df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df = st.data_editor(df, num_rows="dynamic")

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


    df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
    )
    edited_df = st.data_editor(df)

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
