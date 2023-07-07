
from dash import Dash, html, dcc
import pandas as pd
from datetime import datetime,date
import re
import numpy as np

# 两种接口
import plotly_express as px
import plotly.graph_objects as go

treasure = [] 

def scatterGraph():
    df = px.data.gapminder()
    fig = px.scatter(
        df.query("year==2007"),  # 选择绘图数据
        x="gdpPercap",  # x轴
        y="lifeExp",  # y轴
        size="pop",  # 点的大小
        color="continent",  # 颜色
        hover_name="country",  # 悬停信息
        log_x=True,   # 对数变换
        size_max=60  # 点的最大值
    )
    # fig.show()
    return fig

def pmGraph():
    # Task Name,
    # Urgency(DDL),
    # Workload statistics (calculated in hours),
    # " Impact (on a scale of 10)",
    # Preference level,Project significance," Project achievement/gains"
    df = pd.read_csv('treasure.csv')
    today = date.today()
    
    df['DDL'] = (pd.to_datetime(df['Urgency'], format='%Y-%m-%d').dt.date-today).apply(lambda x: int(re.findall(r'\d+', str(x))[0]))
    
    fig = px.scatter(
        df,  # 选择绘图数据
        x="DDL",  # x轴
        y="Impact",  # y轴
        size="Workload",  # 点的大小
        # color="continent",  # 颜色
        hover_name="Name",  # 悬停信息
        log_x=True,   # 对数变换
        size_max=120  # 点的最大值
    )
    # fig.show()
    return fig
    
    

if __name__ == "__main__": 
    
    # fig0 = scatterGraph()
    fig0 = pmGraph()
    
    

    # dash to show
    app = Dash(__name__)
    app.layout = html.Div(children=[
        dcc.Graph(
            id='scatter',
            figure=fig0,
            style = {'height': '100vh'}
        )
    ])
    
    app.run_server(debug=True, host="202.38.72.23")
    
