import pandas as pd
import plotly.express as px
dx=pd.read_csv("data.csv")
graph=px.scatter(dx,x= 'Population',y='Per capita',color='Country',size='Population')
graph.show()