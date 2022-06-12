import pandas as pd
import plotly.graph_objects as go
df=pd.read_csv("C:/Users/mhrat/OneDrive/Desktop/python/c107/data.csv")
data=df.groupby("level")["attempt"].mean()
graph=go.Figure(go.Bar(x=["Level 1","Level 2",'Level 3','Level 4'],y=data))
graph.show()
