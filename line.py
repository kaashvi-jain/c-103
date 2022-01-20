import pandas as pd
import plotly.express as px
dx=pd.read_csv("line_chart.csv")
graph=px.line(dx,x="Year",y="Per capita income",color='Country', title='line chart')
graph.show()