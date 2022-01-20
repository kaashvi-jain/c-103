import pandas as pd
import plotly.express as px
dx=pd.read_csv("data.csv")
graph=px.bar(dx,x='Country',y='InternetUsers')
graph.show()