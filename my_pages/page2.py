import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show():
    st.write("### 🎉 ยินดีต้อนรับสู่หน้า 2")
    st.write("📌 เนื้อหาของหน้า 2")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "Redeem Overall", "Stacked Bar", "Bubble Chart", "Contour Chart",
        "Expenses Table", "Quarterly Table", "Icicle Chart", "2025 Earn", "2025 Redeem"
    ])

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

    with tab1:
        st.subheader("\U0001F4CA Redeem Overall")
        data = {
            "Category": ["A", "B", "C", "D", "E", "F", "G", "H"],
            "Value": [100, 200, 150, 300, 250, 356, 789, 670],
            "Region": ["North", "South", "East", "West", "North", "East", "West", "North"]
        }
        
        df = pd.DataFrame(data)
        df_region_sum = df.groupby("Region")["Value"].sum().reset_index()

        north_total = df_region_sum[df_region_sum["Region"] == "North"]["Value"].sum()
        south_total = df_region_sum[df_region_sum["Region"] == "South"]["Value"].sum()
        east_total = df_region_sum[df_region_sum["Region"] == "East"]["Value"].sum()
        west_total = df_region_sum[df_region_sum["Region"] == "West"]["Value"].sum()

        col1, col2, col3, col4 = st.columns(4)
        create_card(col1, north_total, "North", "#FFCDD2", "#B71C1C", "rgba(183,28,28,0.2)")
        create_card(col2, south_total, "South", "#C8E6C9", "#1B5E20", "rgba(27,94,32,0.2)")
        create_card(col3, east_total, "East", "#BBDEFB", "#0D47A1", "rgba(13,71,161,0.2)")
        create_card(col4, west_total, "West", "#FFF9C4", "#FF6F00", "rgba(255,111,0,0.2)")

        st.sidebar.header("\U0001F50D Filter Data")
        filter_region = st.sidebar.multiselect("\U0001F30E เลือก Region", df["Region"].unique(), default=df["Region"].unique())
        df_filtered = df[df["Region"].isin(filter_region)]

        col_table, col_chart = st.columns([1, 1])
        with col_table:
            st.subheader("\U0001F4CB ข้อมูลตาราง")
            st.dataframe(df_filtered.style.format({"Value": "{:,.0f}"}), use_container_width=True)

        with col_chart:
            st.subheader("\U0001F4C8 กราฟแท่งข้อมูล")
            fig = px.bar(df_filtered, x="Category", y="Value", color="Category",
                         title="\U0001F4CA Bar Chart", labels={"Value": "จำนวน", "Category": "หมวด"},
                         color_discrete_sequence=px.colors.qualitative.Set1)
            fig.update_layout(width=500, height=400, margin=dict(l=20, r=20, t=40, b=20), title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Stacked Bar Chart")
        fig = go.Figure(go.Bar(x=['b', 'a', 'c', 'd'], y=[2,5,1,9], name='Montreal'))
        fig.add_trace(go.Bar(x=['b', 'a', 'c', 'd'], y=[1,4,9,16], name='Ottawa'))
        fig.add_trace(go.Bar(x=['b', 'a', 'c', 'd'], y=[6,8,4.5,8], name='Toronto'))
        fig.update_layout(barmode='stack', xaxis={'categoryorder':'array', 'categoryarray':['d','a','c','b']})
        st.plotly_chart(fig, theme="streamlit")

    with tab3:
        st.subheader("Bubble Chart - GDP vs Life Expectancy")
        gap = px.data.gapminder().query("year == 2007")
        fig = px.scatter(gap, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                         hover_name="country", log_x=True, size_max=60)
        st.plotly_chart(fig, theme="streamlit")

    with tab4:
        st.subheader("Contour Chart")
        fig = go.Figure(data=go.Contour(z=[[10,10.625,12.5,15.625,20],[5.625,6.25,8.125,11.25,15.625],[2.5,3.125,5.,8.125,12.5],[0.625,1.25,3.125,6.25,10.625],[0,0.625,2.5,5.625,10]]))
        st.plotly_chart(fig, theme="streamlit")

    with tab5:
        st.subheader("Expenses Table")
        fig = go.Figure(data=[go.Table(
            columnorder=[1,2],
            columnwidth=[80,400],
            header=dict(values=[["<b>EXPENSES</b><br>as of July 2017"], ["<b>DESCRIPTION</b>"]], fill_color='royalblue', font=dict(color='white', size=12)),
            cells=dict(values=[['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL EXPENSES</b>'],
                                ["Lorem ipsum..." for _ in range(5)]],
                       fill_color=['paleturquoise', 'white'], font_size=12)
        )])
        st.plotly_chart(fig, theme="streamlit")

    with tab6:
        st.subheader("Quarterly Table")
        fig = go.Figure(data=[go.Table(
            header=dict(values=['<b>EXPENSES</b>','<b>Q1</b>','<b>Q2</b>','<b>Q3</b>','<b>Q4</b>'], fill_color='grey', font=dict(color='white', size=12)),
            cells=dict(values=[
                ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
                [1200000, 20000, 80000, 2000, 12120000],
                [1300000, 20000, 70000, 2000, 130902000],
                [1300000, 20000, 120000, 2000, 131222000],
                [1400000, 20000, 90000, 2000, 14102000]
            ], fill_color='lightgrey')
        )])
        st.plotly_chart(fig, theme="streamlit")

    with tab7:
        st.subheader("Icicle Chart")
        vendors = ["A", "B", "C", "D", None, "E", "F", "G", "H", None]
        sectors = ["Tech", "Tech", "Finance", "Finance", "Other", "Tech", "Tech", "Finance", "Finance", "Other"]
        regions = ["North"]*5 + ["South"]*5
        sales = [1, 3, 2, 4, 1, 2, 2, 1, 4, 1]
        df = pd.DataFrame(dict(vendors=vendors, sectors=sectors, regions=regions, sales=sales))
        df["all"] = "all"
        fig = px.icicle(df, path=['all', 'regions', 'sectors', 'vendors'], values='sales')
        fig.update_traces(root_color='lightgrey')
        fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
        st.plotly_chart(fig, theme="streamlit")

    with tab8:
        st.subheader("Sunburst Chart")
        fig = go.Figure(go.Sunburst(
            labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
            parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
            values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
        ))
        fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
        st.plotly_chart(fig, theme="streamlit")

    with tab9:
        st.subheader("Donut & Van Gogh Charts")

        def get_chart_donut():
            labels = ['Oxygen', 'Hydrogen', 'Carbon Dioxide', 'Nitrogen']
            values = [4500, 2500, 1053, 500]
            return go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

        def get_chart_vangogh():
            labels = ['1st', '2nd', '3rd', '4th', '5th']
            night_colors = ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)', 'rgb(36, 55, 57)', 'rgb(6, 4, 4)']
            sunflowers_colors = ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)', 'rgb(129, 180, 179)', 'rgb(124, 103, 37)']
            irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)', 'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
            cafe_colors = ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)', 'rgb(175, 51, 21)', 'rgb(35, 36, 21)']

            specs = [[{'type': 'domain'}, {'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'}]]
            fig = make_subplots(rows=2, cols=2, specs=specs)

            fig.add_trace(go.Pie(labels=labels, values=[38, 27, 18, 10, 7], name='Starry Night', marker_colors=night_colors), 1, 1)
            fig.add_trace(go.Pie(labels=labels, values=[28, 26, 21, 15, 10], name='Sunflowers', marker_colors=sunflowers_colors), 1, 2)
            fig.add_trace(go.Pie(labels=labels, values=[38, 19, 16, 14, 13], name='Irises', marker_colors=irises_colors), 2, 1)
            fig.add_trace(go.Pie(labels=labels, values=[31, 24, 19, 18, 8], name='The Night Café', marker_colors=cafe_colors), 2, 2)

            fig.update_traces(hoverinfo='label+percent+name', textinfo='none')
            fig.update_layout(title_text='Van Gogh: 5 Most Prominent Colors Shown Proportionally', showlegend=False)
            return fig

        st.markdown("### Donut Chart")
        fig1 = get_chart_donut()
        st.plotly_chart(fig1, theme="streamlit")

        st.markdown("### Van Gogh Color Composition (Pie Charts)")
        fig2 = get_chart_vangogh()
        st.plotly_chart(fig2, theme="streamlit")