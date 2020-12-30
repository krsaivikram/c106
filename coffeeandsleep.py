import plotly.express as px
import csv 
with open("C:/Users/Manorama/Desktop/coffee&sleep.csv") as file:
    df = csv.DictReader(file)
    fig = px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()
