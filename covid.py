import pandas as pd
import plotly.express as px
dx=pd.read_csv("covid.csv")
graph=px.scatter(dx,x= 'cases',y='date',color='country')
graph.show()